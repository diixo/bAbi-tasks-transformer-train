from datasets import load_dataset   
from transformers import PreTrainedTokenizer


INPUT_TEMPLATE = """
### Context:
{context}

### Question:
{question}

### System:
{answer}
"""


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


class BabiqaDatasetEval():

    def __init__(self, tokenizer, task_no="qa1", split="train", no_answer=False) -> None:

        dataset = load_dataset('babi_qa', type='en', task_no=task_no, trust_remote_code=True)[split]
        self.data = list(get_next_qa(dataset))

        self.tokenizer: PreTrainedTokenizer = tokenizer
        self.no_answer = no_answer


    def get_object(self, index):
        context, question, answer = self.data[index]
        return {
            "context": context,
            "question": question,
            "answer": answer
        }


    def __getitem__(self, index):
        context, question, answer = self.data[index]
        cqa = {
            "context": context,
            "question": question,
            "answer": answer
        }

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

