import json, math
from collections import defaultdict, Counter

def build_index():
    with open("data/tokens.json") as f:
        tokens_per_doc = json.load(f)
    
    N = len(tokens_per_doc)
    df = defaultdict(int)

    for tokens in tokens_per_doc.values():
        unique_tokens = set(tokens)
        for token in unique_tokens:
            df[token] += 1

    tfidf_index = defaultdict(dict)

    for doc, tokens in tokens_per_doc.items():
        total_terms = len(tokens)
        tf = Counter(tokens)

        
        for term, count in tf.items():
            tf_score = count / total_terms
            idf_score = math.log(N / df[term])
            tfidf_score = tf_score * idf_score
            tfidf_index[term][doc] = round(tfidf_score, 6)

    with open("data/inverted_index.json", "w") as f:
        json.dump(tfidf_index, f)

if __name__ == "__main__":
    build_index()
