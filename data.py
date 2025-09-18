from datasets import load_dataset   
from transformers import PreTrainedTokenizer
from torch.nn.utils.rnn import pad_sequence
from collections import defaultdict
import json


INPUT_TEMPLATE = """
### Context:
{context}

### Question:
{question}

### Answer:
{answer}
"""


def load_babi_jsonl(file_path: str) -> list:
    items = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line:
                item = json.loads(line)
                items.append((item["context"], item["input"], item["output"]))
    return items


def get_next_qa(dataset):
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
                    yield context, question, answer
                else:
                    context += f" {sent}"


class BabiQADataset():

    def __init__(self, tokenizer, task_no="qa1", split="train", no_answer=False, return_object=False) -> None:
        self.data = list()
        if task_no == "ext":
            if split in {"train", "test",}:
                self.data = load_babi_jsonl(f"datasets/qa-ext_{split}.jsonl")
        else:
            dataset = load_dataset('babi_qa', type='en', task_no=task_no, trust_remote_code=True)[split]
            self.data = list(get_next_qa(dataset))

        self.tokenizer: PreTrainedTokenizer = tokenizer
        self.no_answer = no_answer
        self.return_object = return_object


    def __getitem__(self, index):
        context, question, answer = self.data[index]
        cqa = {
            "context": context,
            "question": question,
            "answer": answer
        }
        
        if self.return_object:
            return cqa

        if self.no_answer:
            cqa["answer"] = ""
        
        input_text = INPUT_TEMPLATE.format_map(cqa).strip()
        encodings = self.tokenizer(input_text, truncation=True, max_length=384, return_tensors="pt")
        encodings["labels"] = encodings["input_ids"].clone()
        return {
            "input_ids": encodings["input_ids"],
            "labels": encodings["labels"]
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

