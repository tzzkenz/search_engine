import json
from collections import defaultdict

def build_index():
    with open("data/tokens.json") as f:
        tokens_per_doc = json.load(f)

    index = defaultdict(list)
    for doc, tokens in tokens_per_doc.items():
        for token in set(tokens):
            index[token].append(doc)

    with open("data/inverted_index.json", "w") as f:
        json.dump(index, f)

if __name__ == "__main__":
    build_index()
