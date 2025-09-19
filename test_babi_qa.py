
from datasets import load_dataset, load_dataset_builder


if __name__ == "__main__":

    dataset = load_dataset("babi_qa/hf_babi_qa.py", type="en", task_no = "qa1", trust_remote_code=True)
    train_ds = dataset["train"]
    test_ds = dataset["test"]

    builder = load_dataset_builder("babi_qa/hf_babi_qa.py", "en-qa1")

    filepath = "babi_qa/test-items.txt"
    files = [(filepath, open(filepath, "rb"))]

    for key, value in builder._generate_examples(filepath=filepath, files=files):
        print("Key:", key)
        print("Value:", value)
