from datasets import load_dataset   
from transformers import PreTrainedTokenizer
from torch.nn.utils.rnn import pad_sequence
from collections import defaultdict
from utils import parse_to_slots
import torch


def format_context_to_slots(context):
    slots = parse_to_slots(context)
    input_str = f"### Context:\n{context}\n\n"
    output_str = f"### Slots:\n{slots}"
    return input_str, output_str


def format_question_to_answer(context, question, answer):
    slots = parse_to_slots(context)
    input_str = f"### Context:\n{question}\n\n### Slots:\n{slots}\n\n"
    output_str = f"### System:\n{answer}"
    return input_str, output_str


def make_items_list(dataset) -> list:
    """
    return list(tuple(context, question, answer))
    """
    items = list()
    for x in dataset:
        story = x.get('story', None)
        if story:
            sentences = story.get("text", None)
            sent_types = story.get("type",[])
            
            context = ""
            for s_idx, sent in enumerate(sentences):
                if sent_types[s_idx] == 1:
                    question = sent
                    answer = story["answer"][s_idx]
                    context = context.strip()

                    # 1. context -> slots
                    input_1, output_1 = format_context_to_slots(context)
                    items.append((input_1, output_1))

                    # 2. slots + question -> answer
                    input_2, output_2 = format_question_to_answer(context, question, answer)
                    items.append((input_2, output_2))
                else:
                    context += f" {sent}"
    return items


class BabiqaDatasetSlots():

    def __init__(self, tokenizer, task_no="qa1", split="train", ext=False) -> None:
        self.tokenizer: PreTrainedTokenizer = tokenizer
        self.data = list()

        type_sz = "en-10k" if ext else "en"
        dataset = load_dataset("babi_qa", type=type_sz, task_no=task_no, trust_remote_code=True)[split]
        self.data = make_items_list(dataset)


    def __getitem__(self, index):
        # input_text as context, output_text as target_text        
        input_text, output_text = self.data[index]

        enc_input = self.tokenizer(input_text, truncation=True, add_special_tokens=False, return_tensors="pt")["input_ids"]
        enc_output = self.tokenizer(output_text, truncation=True, add_special_tokens=False, return_tensors="pt")["input_ids"]

        # combine into one sequence
        input_ids = torch.cat([
            enc_input,                                                      # (1, N)
            enc_output,                                                     # (1, M)
            torch.tensor([[self.tokenizer.eos_token_id]], dtype=torch.long) # (1, 1)
        ], dim=1)                                                           # (1, N+M+1)=shape([0],[1])

        # create new array
        labels = input_ids.clone()

        # masked only input_text:   [0, :N=enc_input(1, N)]
        labels[0, :enc_input.size(1)] = -100

        batch_max_length = max(len(item)+1 for item in input_ids)
        assert batch_max_length <= 1024, f"batch_max_length={batch_max_length}<=1024: out of range"

        return {
            "input_ids": input_ids,
            "labels": labels,
        }

    def __len__(self):
        return len(self.data)


def collate_data(batch, padding_value, label_padding_value=-100):

    new_batch = defaultdict(lambda:[])
    for x in batch:
        for x_key in x.keys():
            new_batch[x_key].append(x[x_key][0])
    
    new_batch = dict(new_batch)

    for batch_key in new_batch.keys():
        if batch_key == "labels":
            new_batch[batch_key] = pad_sequence(new_batch[batch_key], batch_first=True, padding_value=label_padding_value)
        else:
            new_batch[batch_key] = pad_sequence(new_batch[batch_key], batch_first=True, padding_value=padding_value)

    if "input_ids" in new_batch:
        new_batch["attention_mask"] = (new_batch["input_ids"] != padding_value).long()

    return new_batch

