import evaluate
from transformers import AutoModelForCausalLM, AutoTokenizer
from data_slots import BabiQADatasetSlots
from utils import parse_answer
import torch
import pandas as pd
import os


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model_dir = "my-model"

tokenizer = AutoTokenizer.from_pretrained(model_dir)
model = AutoModelForCausalLM.from_pretrained(model_dir)
model.to(device)

for task_id in range(1):
    task_no = f"qa{task_id+1}"
    test_dataset = BabiQADatasetSlots(tokenizer, split="test", task_no=task_no)
    test_dataset_raw = BabiQADatasetSlots(
        tokenizer, split="test", retrun_object=True, task_no=task_no
    )
    df = pd.DataFrame(
        columns=["context", "question", "answer", "pred", "correct_or_not"]
    )

    model_prediction = []
    references = []

    for data_idx, data in enumerate(test_dataset):
        raw_data = test_dataset_raw[data_idx]
        output_text = tokenizer.decode(
            model.generate(
                data["input_ids"].to(device),
                max_new_tokens=30,
                do_sample=False,
                eos_token_id=tokenizer.eos_token_id,
                pad_token_id=tokenizer.eos_token_id,
            )[0]
        )

        pred = 0
        pred_words = set(
            parse_answer(output_text, eos_token=tokenizer.eos_token).split()
        )
        label = 1

        answers = set(raw_data["answer"].split())
        if len(pred_words.intersection(answers)) == len(answers):
            pred = 1

        model_prediction.append(pred)
        references.append(label)

        print(data_idx, raw_data["answer"], pred_words)
        df = pd.concat(
            [
                df,
                pd.DataFrame(
                    [
                        {
                            "context": raw_data["context"],
                            "question": raw_data["question"],
                            "answer": raw_data["answer"],
                            "pred": ",".join(list(pred_words)),
                            "correct_or_not": "correct" if pred == 1 else "incorrect",
                        }
                    ]
                ),
            ],
            ignore_index=True,
        )

        # if data_idx == 30:
            # break

    metric = evaluate.load_metric("accuracy")
    accuracy = metric.compute(predictions=model_prediction, references=references)
    print(task_no, accuracy)
    acc = accuracy["accuracy"]
    os.makedirs("eval_result",exist_ok=True)
    df.to_csv(f"eval_result/{task_no}_{round(acc*100,2)}.csv")
