
from datasets import load_dataset, load_dataset_builder
import json
from collections import defaultdict


BABI_QA_SLOTS_DIR = "babi_qa_slots/"


if __name__ == "__main__":

    dataset = load_dataset(BABI_QA_SLOTS_DIR + "babi_qa_slots.py", type="en", task_no = "qa1", trust_remote_code=True)
    train_ds = dataset["train"]
    test_ds = dataset["test"]

    builder = load_dataset_builder(BABI_QA_SLOTS_DIR + "babi_qa_slots.py", "en-qa1")

    filepath = BABI_QA_SLOTS_DIR + "test-items.txt"
    files = [(filepath, open(filepath, "rb"))]

    stories = []

    for id, dictionary in builder._generate_examples(filepath=filepath, files=files):
        raw_story = dictionary["story"]
        # defaultdict: creates an empty list the first time the key is accessed
        item = defaultdict(list)

        for line in raw_story:
            for k, v in line.items(): item[k].append(v)

        # Let's convert it back to a regular dict
        story = dict(item)
        #print("---------------------------------------\nitem:", story)
        stories.append(story)

    train_ds = builder.raw_to_json()["train"]

    with open(BABI_QA_SLOTS_DIR + "test-items.json", "w", encoding="utf-8") as f:
        json.dump(train_ds, f, ensure_ascii=False, indent=2)

    # dataset = load_dataset('babi_qa', type='en', task_no="qa1", trust_remote_code=True)
    # print(len(dataset["train"]))
