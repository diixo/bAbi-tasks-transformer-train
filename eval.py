import evaluate
from transformers import AutoModelForCausalLM, AutoTokenizer
from data_eval import BabiqaDatasetEval
from utils import parse_answer
import torch
import pandas as pd
import os


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model_dir = "gpt2-babi"

tokenizer = AutoTokenizer.from_pretrained(model_dir)
model = AutoModelForCausalLM.from_pretrained(model_dir)
model.to(device)


if __name__ == "__main__":
#for task_id in range(1):
    #task_no = f"qa{task_id+1}"
    task_no = "qa2"
    test_dataset = BabiqaDatasetEval(tokenizer, split="test", task_no=task_no, no_answer=True)

    df = pd.DataFrame(
        columns=["context", "question", "answer", "pred", "correct_or_not"]
    )

    model_prediction = []
    references = []
    correct = 0

    for data_idx, data in enumerate(test_dataset):
        raw_data = test_dataset.get_object(data_idx)
        input_ids = data["input_ids"].to(device)
        gen_ids = model.generate(
                input_ids=input_ids,
                attention_mask=torch.ones(input_ids.shape, dtype=torch.long, device=input_ids.device),
                max_new_tokens=30,
                do_sample=False,
                eos_token_id=tokenizer.eos_token_id,
                pad_token_id=tokenizer.eos_token_id
            )[0]
        output_text = tokenizer.decode(gen_ids, skip_special_tokens=True)

        pred = 0
        pred_words = set(
            parse_answer(output_text, eos_token=tokenizer.eos_token).split()
        )

        answers = set(raw_data["answer"].split())
        if len(pred_words.intersection(answers)) == len(answers):
            pred = 1

        correct += pred
        model_prediction.append(pred)
        references.append(1)

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


    metric = evaluate.load("accuracy")
    accuracy = metric.compute(predictions=model_prediction, references=references)
    print(f"dataset={task_no},", accuracy, f"correct/all: {correct}/{len(model_prediction)}")
    acc = accuracy["accuracy"]
    os.makedirs("eval-results", exist_ok=True)
    df.to_csv(f"eval-results/{task_no}_{round(acc*100, 2)}.csv")
