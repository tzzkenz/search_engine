import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import os,json

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('punkt_tab')

def clean_text():
    stop_words = set(stopwords.words('english'))
    tokens_per_doc = {}

    for filename in os.listdir("data/pages"):
        with open(f"data/pages/{filename}", encoding='utf-8') as f:
            text = f.read()
        tokens = word_tokenize(text.lower())
        filtered = [w for w in tokens if w.isalnum() and w not in stop_words]
        tokens_per_doc[filename] = filtered

    with open("data/tokens.json", "w") as f:
        json.dump(tokens_per_doc, f)

