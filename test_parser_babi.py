
from data_slots import parse_to_slots


actions = [
    "Mary moved to the bathroom.",
    "John went to the hallway.",
    "Daniel went back to the hallway.",
    "Sandra moved to the garden.",
]

#################################################

context = ""

slots = parse_to_slots(" ".join(actions))
print(slots)

training_examples = [slots]

#################################################
from transformers import GPT2Tokenizer

# Пример токенизации
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
tokenizer.pad_token = tokenizer.eos_token


batch = tokenizer(training_examples,
                  padding=True,
                  truncation=True,
                  return_tensors="pt")

input_ids = batch["input_ids"]
attn_mask = batch["attention_mask"]

labels = input_ids.clone()

# 1) Masking of paddings
labels[attn_mask == 0] = -100

# 2) Masks before "###slots"
for i, text in enumerate(training_examples):
    # находим границу контекста
    context_len = text.find("###slots")
    if context_len == -1:
        continue

    # токенизируем только часть до "###slots"
    tokens_to_ignore = tokenizer(
        text[:context_len],
        add_special_tokens=False
    )["input_ids"]

    # маскируем именно эти токены
    labels[i, :len(tokens_to_ignore)] = -100

    item_idxs = input_ids[i].tolist()
    item_lbls = labels[i].tolist()
    item_mask = attn_mask[i].tolist()

    print("Full input_ids:", item_idxs)
    print("Full lbls_ids:", item_lbls)
    print("Full attn_ids:", item_mask)
    print(text + "\n*****************************")
