
from datasets import load_dataset, load_dataset_builder
import json
from collections import defaultdict


if __name__ == "__main__":

    dataset = load_dataset("babi_qa/babi_qa_slots.py", type="en", task_no = "qa1", trust_remote_code=True)
    train_ds = dataset["train"]
    test_ds = dataset["test"]

    builder = load_dataset_builder("babi_qa/babi_qa_slots.py", "en-qa1")

    filepath = "babi_qa/test-items.txt"
    files = [(filepath, open(filepath, "rb"))]

    stories = []

    for id, dictionary in builder._generate_examples(filepath=filepath, files=files):
        raw_story = dictionary["story"]

        # defaultdict: creates an empty list the first time the key is accessed
        item = defaultdict(list)

        for line in raw_story:
            for k, v in line.items():
                item[k].append(v)

        # Let's convert it back to a regular dict
        story = dict(item)

        print("---------------------------------------\nitem:", story)
        stories.append(story)


    with open("babi_qa/test-items.json", "w", encoding="utf-8") as f:
        json.dump(stories, f, ensure_ascii=False, indent=2)
