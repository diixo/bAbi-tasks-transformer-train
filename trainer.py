from transformers import AutoModelForCausalLM, AutoTokenizer, TrainingArguments, Trainer as DefaultTrainer
from data_slots import BabiQADatasetSlots, collate_data
from torch.utils.data import ConcatDataset
import torch
from transformers.optimization import get_scheduler
import sys
import argparse


def create_test_args() -> list:
    return [
        "trainer.py",
        "gpt2",
        #"-dataset", "ext", # switch ext->babi
        "-lr", "2e-4",
        "-epoch", "5",
        "-batch_size", "8",
    ]


parser = argparse.ArgumentParser()
parser.add_argument("model_name_or_id")
parser.add_argument("-dataset", default="qa", type=str)
parser.add_argument('-lr', default=3e-4, type=float)
parser.add_argument('-batch_size', default=6, type=int)
parser.add_argument('-epoch', default=3, type=int)
parser.add_argument('-ga', '--gradient_accumulation', default=1, type=int)


class Trainer(DefaultTrainer):
    def create_scheduler(self, num_training_steps: int, optimizer: torch.optim.Optimizer = None):
        """
        disable scheduler
        """
        if self.lr_scheduler is None:
            self.lr_scheduler = get_scheduler(
                self.args.lr_scheduler_type,
                optimizer=self.optimizer if optimizer is None else optimizer,
                num_warmup_steps=0,
                num_training_steps=sys.maxsize,
            )
        return self.lr_scheduler


def make_dataset(tasks_amount=0, dataset="default"):
    if tasks_amount == 0:
        tasks_amount = 20
    train_ds = ConcatDataset(
        [
            BabiQADatasetSlots(tokenizer, split="train", task_no=f"qa{task_id+1}")
            for task_id in range(tasks_amount)
        ]
    )
    test_ds = ConcatDataset(
        [
            BabiQADatasetSlots(tokenizer, split="test", task_no=f"qa{task_id+1}")
            for task_id in range(tasks_amount)
        ]
    )
    return train_ds, test_ds


if __name__ == "__main__":
    sys.argv = create_test_args()
    args = parser.parse_args()

    tokenizer = AutoTokenizer.from_pretrained(args.model_name_or_id)
    model = AutoModelForCausalLM.from_pretrained(args.model_name_or_id)

    train_dataset, test_dataset = make_dataset(1, args.dataset)

    training_args = TrainingArguments(
        output_dir="my_model",
        save_strategy="epoch",
        eval_strategy="epoch",
        learning_rate=args.lr,
        num_train_epochs=args.epoch,
        weight_decay=0.0,
        push_to_hub=False,
        load_best_model_at_end=True,
        per_device_train_batch_size=args.batch_size,
        gradient_accumulation_steps=args.gradient_accumulation
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
        eval_dataset=test_dataset,
        data_collator=lambda x: collate_data(
            x,
            padding_value=tokenizer.eos_token_id,
            label_padding_value=tokenizer.eos_token_id
        ),
    )

    trainer.train()
    trainer.save_model("my_model/best")
    tokenizer.save_pretrained("my_model/best")
