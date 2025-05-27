# 🔎 SearchEngineLite

SearchEngineLite is a lightweight, educational search engine prototype built in Python. It demonstrates the core components of a search engine — crawling, indexing using TF-IDF, and querying with a simple interface and metadata-based results.

---

## 📌 Features

- 🌐 Web crawler that extracts content and metadata from pages
- 🧹 Preprocessing with tokenization and basic filtering
- 🧠 Inverted Index with TF-IDF scores for efficient search
- 🔍 Query interface that ranks documents using TF-IDF relevance
- 📄 Snippets and titles extracted for each result
- 📁 Clean project structure with metadata and pages saved separately

---

## 🛠️ Project Structure

```
SearchEngineLite/
├── data/
│   ├── pages/              # Raw HTML content
│   ├── metadata/           # JSON files with title, snippet, URL
│   ├── tokens.json         # Preprocessed tokens per document
│   └── inverted_index.json # TF-IDF index
├── crawl.py                # Crawler script
├── indexer.py              # Builds inverted index using TF-IDF
├── search.py               # Query engine
├── utils.py                # Tokenizer & helper functions (optional)
└── README.md               # Project documentation
```

---

## 🔧 How It Works

### 1. Crawl
- Starts from a seed URL
- Extracts and saves page content and metadata (title, snippet, URL)
- Ignores duplicate URLs and non-HTML resources

### 2. Preprocess
- Converts text to lowercase
- Removes punctuation and common stopwords
- Tokenizes words (soon to include stemming/lemmatization)

### 3. Index
- Builds an inverted index with TF-IDF scores
- Stored as a JSON file for querying

### 4. Search
- Accepts a query string
- Tokenizes and matches query terms
- Ranks documents based on total TF-IDF score
- Returns top results with metadata

---

## 🧪 Example Usage

```bash
python crawl.py     # Crawls and saves pages
python indexer.py   # Builds TF-IDF index
python search.py    # Search from terminal
```

In `search.py`:

```python
print(search("web development"))
```

Returns:

```json
{
  "3.html": {
    "title": "Modern Web Dev",
    "url": "https://example.com",
    "snippet": "Web development is the work involved in developing a website..."
  }
}
```

---

## 🧱 Dependencies

Install with pip:

```bash
pip install beautifulsoup4 requests nltk
```

---

## 📌 What's Next

- [x] Improved crawling logic
- [x] TF-IDF-based inverted index
- [x] Snippet + title-based search output
- [x] Advanced preprocessing (stemming, stopwords)
- [ ] Cosine similarity
- [ ] Web frontend (Flask/Streamlit)
- [ ] Synonym support

---

## 🧑‍💻 Author

Made with ❤️ by **Kenz E S**

*Project idea: Learning by building a minimal functional search engine.*
