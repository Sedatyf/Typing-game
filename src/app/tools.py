import json
import os
import random

current_path = os.path.dirname(os.path.realpath(__file__))
sources_path = os.path.join(current_path, "sources.json")


def pick_text():
    with open(sources_path, "r") as f:
        json_text = json.load(f)

    text_list = []
    
    for _, value in json_text.items():
        text_list.append(value)
    
    random_text = random.choice(text_list)
    return random_text


if __name__ == "__main__":
    pick_text()