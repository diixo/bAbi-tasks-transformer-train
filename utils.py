import re

def remove_punctuation_wo_comma(text):
    cleaned_text = re.sub(r"[^\w\s!,]", "", text)
    return cleaned_text


def parse_answer(text: str, eos_token):
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


def story_to_slots(story: str, objects=("football", "milk", "apple"), normalization = False) -> str:
    """
    Output string format:
    Person1=location:location-1; Person2=location:location-2; Person3=location:location-3;
    """
    slots = {}
    holders = {}

    for line in story.strip().split("."):
        line = line.strip()

        # убираем номер в начале
        if re.match(r"^\d+", line):
            line = " ".join(line.split()[1:])

        # перемещение персонажа
        m = re.match(r"(\w+) (moved|journeyed|went|travelled).* to the (\w+)", line)
        if m:
            name, _, place = m.groups()
            slots[name] = {"location": place}
            # обновляем предметы, которые у этого персонажа
            # TODO: ??? не меняем локацию предметов владельца, чтобы модель сама догадалась по аттрибуту with?
            if normalization:
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
            if re.search(fr"(\w+) (dropped|left|discarded|put down) the {obj}", line):
                name = line.split()[0]
                if holders.get(obj) == name:
                    del holders[obj]
                    # TODO:
                    # объект остаётся в текущей локации персонажа
                    if name in slots:
                        if "location" in slots[name]:
                            slots[obj] = {"location": slots[name]["location"]}

    # финальная нормализация: все "with" → "location"
    if normalization:
        for obj, state in slots.items():
            if "with" in state:
                holder = state["with"]
                if holder in slots and "location" in slots[holder]:
                    slots[obj] = {"location": slots[holder]["location"]}

    # print(story)
    # print(slots)
    return dict_to_str(slots)


def str_to_slots(line: str, objects=("football", "milk", "apple")):
        line = line.strip()

        m = re.match(r"(\w+) (moved|journeyed|went|travelled).* to the (\w+)", line)
        if m:
            name, _, place = m.groups()
            return [ name, "location", place, ]

        for obj in objects:
            if re.search(fr"(\w+) (got|took|grabbed|picked up) the {obj}", line):
                name = line.split()[0]
                return [ obj, "with", name ]

        for obj in objects:
            if re.search(fr"(\w+) (dropped|left|discarded|put down) the {obj}", line):
                name = line.split()[0]
                return [ obj, "with", ""]


def test():

    story = """
Daniel went to the bathroom.
Sandra journeyed to the garden.
 Mary moved to the hallway.
 Daniel grabbed the football there.
 Mary travelled to the bathroom.
 Mary got the apple there.
 Mary went to the bedroom.
 Daniel journeyed to the bedroom.
 Daniel discarded the football.
 Mary travelled to the hallway.
 John journeyed to the kitchen.
 Sandra took the football there.
 Sandra dropped the football.
 Sandra moved to the office.
 John journeyed to the hallway."""

    slots = story_to_slots(story)
    print(slots)

    for line in story.strip().split("."):
        if line:
            slots = str_to_slots(line)
            print(line)
            print(slots)


if __name__ == "__main__":
    test()
