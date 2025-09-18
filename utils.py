import re

def remove_punctuation_wo_comma(text):
    cleaned_text = re.sub(r"[^\w\s!,]", "", text)
    return cleaned_text


def parse_answer(text: str,eos_token):
    text = text.replace(eos_token,"")
    try:
        answer_start = text.index("System:")
        answer = remove_punctuation_wo_comma(text[answer_start:].split(":")[1].strip().split("\n")[0])
    except:
        answer = ""
    return answer


def str_tokenize_words(s: str):
    import re
    s = re.findall("(\.?\w[\w'\.&-]*\w|\w\+*#?)", s)
    if s: return s
    return []


def dict_to_str(dictionary: dict):
    slot_str = " ".join(
        f"{name}=" + " ".join(f"{k}:{v};" for k, v in attrs.items())
        for name, attrs in dictionary.items()
    )
    return slot_str


persons = { "Sandra", "Daniel", "John", "Mary", }
locations = { "office", "garden", "hallway", "bedroom", "bathroom", }


def parse_to_slots(context: str) -> str:
    """
    Output string format:
    Person1=location:location-1; Person2=location:location-2; Person3=location:location-3;
    """
    words = str_tokenize_words(context)
    person = None
    slot_list = {}
    for w in words:
        if w in persons:
            person = w
        if w in locations and person is not None:
            slot_list[person] = { "location": w }

    return dict_to_str(slot_list)



def parse_sequence_slots(story: str, objects=("football", "milk", "apple")):
    slots = {}
    holders = {}  # какой предмет у кого
    
    for line in story.strip().split("\n"):
        # убираем номер в начале
        line = line.strip()
        print(line)
        if re.match(r"^\d+", line):
            line = " ".join(line.split()[1:])

        # перемещение персонажа
        m = re.match(r"(\w+) (moved|journeyed|went|travelled).* to the (\w+)", line)
        if m:
            name, _, place = m.groups()
            slots[name] = {"location": place}
            # обновляем предметы, которые у этого персонажа
            for obj, holder in holders.items():
                if holder == name:
                    slots[obj] = {"location": place}

        # персонаж взял объект
        for obj in objects:
            if re.search(fr"(\w+) (got|took|grabbed|picked up) the {obj}", line):
                name = line.split()[0]
                holders[obj] = name
                slots[obj] = {"with": name}

        # персонаж положил объект
        for obj in objects:
            if re.search(fr"(\w+) (dropped|left) the {obj}", line):
                name = line.split()[0]
                if holders.get(obj) == name:
                    del holders[obj]
                    # объект остаётся в текущей локации персонажа
                    slots[obj] = {"location": slots[name]["location"]}

    # финальная нормализация: все "with" → "location"
    for obj, state in slots.items():
        if "with" in state:
            holder = state["with"]
            if holder in slots and "location" in slots[holder]:
                slots[obj] = {"location": slots[holder]["location"]}

    print(slots)
    return dict_to_str(slots)


def test():

    story = """Mary went back to the kitchen.
Mary moved to the bathroom.
Mary went back to the bedroom.
Daniel went to the garden.
Daniel went to the bathroom.
John moved to the bedroom.
John went back to the office.
John moved to the bathroom.
Daniel went back to the garden.
Daniel took the milk there.
John went back to the hallway.
Daniel travelled to the hallway.
"""

    slots = parse_sequence_slots(story)
    print(slots)

test()
