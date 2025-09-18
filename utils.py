import re

def remove_punctuation_wo_comma(text):
    cleaned_text = re.sub(r"[^\w\s!,]", "", text)
    return cleaned_text


def parse_answer(text: str,eos_token):
    text = text.replace(eos_token,"")
    try:
        answer_start = text.index("Answer:")
        answer = remove_punctuation_wo_comma(text[answer_start:].split(":")[1].strip().split("\n")[0])
    except:
        answer = ""
    return answer


def str_tokenize_words(s: str):
    import re
    s = re.findall("(\.?\w[\w'\.&-]*\w|\w\+*#?)", s)
    if s: return s
    return []


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

    slot_str = " ".join(
        f"{name}=" + " ".join(f"{k}:{v};" for k, v in attrs.items())
        for name, attrs in slot_list.items()
    )
    return slot_str
