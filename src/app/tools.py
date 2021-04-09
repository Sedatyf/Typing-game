import json
import os
import random

current_path = os.path.dirname(os.path.realpath(__file__))
sources_path = os.path.join(current_path, "sources.json")


def pick_text():
    with open(sources_path, "r") as f:
        json_text = json.load(f)

    text_list = []
    texts = json_text.get("texts")
    for item in texts:
        text_list.append(item["text"])
    
    return random.choice(text_list)


def write_to_sources(title, author, text, type):
    with open(sources_path) as f:
        json_data = json.load(f)

        json_data_from_list = json_data["texts"]
        item_to_add = {
            "title": title,
            "author": author,
            "text": text,
            "work_type": type
        }
        json_data_from_list.append(item_to_add)
    with open(sources_path, "w") as f:
        json.dump(json_data, f, indent=4, ensure_ascii=False)


def retrieve_text_indice(filepath, text_to_retrieve):
    with open(filepath, "r") as f:
        json_file = json.load(f)

    text_list = []
    texts = json_file.get("texts")
    for item in texts:
        text_list.append(item["text"])
    
    return text_list.index(text_to_retrieve)


if __name__ == "__main__":
    #pick_text()
    write_to_sources("temp_title", "temp_author", "temp_text", "other")