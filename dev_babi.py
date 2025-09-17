
def str_tokenize_words(s: str):
    import re
    s = re.findall("(\.?\w[\w'\.&-]*\w|\w\+*#?)", s)
    if s: return s
    return []


actions = [
    "Mary moved to the bathroom.",
    "John went to the hallway.",
    "Daniel went back to the hallway.",
    "Sandra moved to the garden."
]

persons = { "Sandra", "Daniel", "John", "Mary", }

locations = { "office", "garden", "hallway", "bedroom", "bathroom", }

slots = {}


def make_slots_set(event, slot_list):
    words = str_tokenize_words(event)

    person = ""
    for w in words:
        if w in persons:
            person = w

        if w in locations:
            slot_list[person] = { "location": w }
    return slot_list

#################################################
training_examples = []
context = ""

for action in actions:

    context += f"###context: {action}\n"

    slots = make_slots_set(action, slots.copy())

    example_text = (
        context +
        "###slots " + str(slots) + "\n" +
        "###system " + "OK.\n"   # Stub of answer
    )
    #print(example_text)
    training_examples.append(example_text)

print(slots)

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
