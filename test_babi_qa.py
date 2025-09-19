from babi_qa.hf_babi_qa import BabiQa, BabiQaConfig


if __name__ == "__main__":

    builder = BabiQa(config=BabiQaConfig(type="shuffled-10k", task_no="qa1"))
    dataset = builder.as_dataset()
    print(dataset["train"][0])
