import json

def search(query):
    with open("data/inverted_index.json") as f:
        index = json.load(f)

    query_tokens = query.lower().split()
    scores = {}
    metadata = {}

    for token in query_tokens:
        docs = index.get(token, [])
        for doc in docs:
            scores[doc] = scores.get(doc, 0) + 1

    sorted_docs = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    
    for doc, _ in sorted_docs[:5]:
        doc_id = doc.split(".")[0]
        with open(f"data/metadata/{doc_id}.json") as f:
            doc_data = json.load(f)
            metadata[f"{doc_id}.html"] = doc_data

    return metadata

print(search("web"))

