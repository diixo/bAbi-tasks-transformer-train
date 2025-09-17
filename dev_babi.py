

def str_tokenize_words(s: str):
    import re
    s = re.findall("(\.?\w[\w'\.&-]*\w|\w\+*#?)", s)
    if s: return s
    return []

# Список событий
events = [
    "Mary moved to the bathroom.",
    "John went to the hallway.",
    "Daniel went back to the hallway.",
    "Sandra moved to the garden."
]

locations = {"office", "garden", "hallway", "bedroom", "bathroom",}

# Инициализируем belief state
belief_state = {}

# Функция для обновления слотов персонажей
def update_belief_state(event, belief_state):
    words = str_tokenize_words(event)
    # Берём имя персонажа (первое слово)
    character = words[0]
    # Находим местоположение (после 'to')
    for id, w in enumerate(words):
        if w in locations:
            belief_state[character] = { "location": words[id] }
    return belief_state

# Проходим по всем событиям
for e in events:
    belief_state = update_belief_state(e, belief_state.copy())
    #print(f"After event: '{e}'\nBelief state: {belief_state}\n")


training_examples = []
context = ""

for e in events:
    # Добавляем событие в контекст
    context += f"###ctx: {e}\n"
    # Обновляем belief state
    belief_state = update_belief_state(e, belief_state.copy())
    # Создаём пример для GPT-2
    example_text = (
        context +
        "###slots " + str(belief_state) + "\n" +
        "###sys " + "OK.\n"   # Заглушка для ответа, можно заменить на реальный system response
    )
    #print(example_text)
    training_examples.append(example_text)

################################################
from transformers import GPT2Tokenizer

# Пример токенизации
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
tokenizer.pad_token = tokenizer.eos_token


encodings = tokenizer(training_examples, return_tensors="pt", padding=True, truncation=True)
input_ids = encodings["input_ids"]
attention_mask = encodings["attention_mask"]

# Labels для causal LM: игнорируем токены контекста
labels = input_ids.clone()
for i, text in enumerate(training_examples):
    context_len = text.find("###slots")
    tokens_to_ignore = tokenizer(text[:context_len])["input_ids"]
    labels[i, :len(tokens_to_ignore)] = -100
    # lbl = labels[i,:]
    # print(lbl)
    # print(text)
    # print()

# Теперь input_ids + labels можно использовать для SFT тренировки GPT-2
print("Input IDs shape:", input_ids.shape)
print("Labels shape:", labels.shape)

######### correct paddings #########

batch = tokenizer(training_examples,
                  padding=True,
                  truncation=True,
                  return_tensors="pt")

input_ids = batch["input_ids"]
attn_mask = batch["attention_mask"]

labels = input_ids.clone()

# 1) Маскируем паддинги
labels[attn_mask == 0] = -100

# 2) Маскируем контекст до "###slots"
for i, text in enumerate(training_examples):
    # находим границу контекста
    context_len = text.find("###slots")
    if context_len == -1:
        continue  # если маркер не найден — пропускаем

    # токенизируем только часть до "###slots"
    tokens_to_ignore = tokenizer(text[:context_len], add_special_tokens=False)["input_ids"]

    # маскируем именно эти токены
    labels[i, :len(tokens_to_ignore)] = -100

    # как вывести массив индексов для конкретного... 
    print("Full input_ids:", input_ids[i].tolist())
    print("Full lbls_ids:", labels[i].tolist())
    print("Full attn_ids:", attn_mask[i].tolist())
    print(text)
    print()