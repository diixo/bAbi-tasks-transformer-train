
from datasets import load_dataset, load_dataset_builder
import json
from collections import defaultdict


BABI_QA_SLOTS = "babi_qa_slots/babi_qa_slots.py"


if __name__ == "__main__":

    builder = load_dataset_builder(BABI_QA_SLOTS, "en-qa1")

    filepath = "babi_qa_slots/test-items.txt"
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

    # need to unzip tasks archive
    #train_ds = builder.raw_to_json()["train"]

    # with open("datasets/test-items.json", "w", encoding="utf-8") as f:
    #     json.dump(train_ds, f, ensure_ascii=False, indent=2)

    dataset = load_dataset('babi_qa', type='en', task_no="qa1", trust_remote_code=True)
    print(len(dataset["train"]))

    dataset = load_dataset(BABI_QA_SLOTS, type="en", task_no = "qa1", trust_remote_code=True)
    print(len(dataset["train"]))
