import json

def search(query):
    with open("data/inverted_index.json") as f:
        index = json.load(f)

    query_tokens = query.lower().split()
    scores = {}
    for token in query_tokens:
        docs = index.get(token, [])
        for doc in docs:
            scores[doc] = scores.get(doc, 0) + 1

    sorted_docs = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    return sorted_docs[:5]
