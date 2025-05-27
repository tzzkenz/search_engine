import requests, os, json, time
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urldefrag

def crawl(seed_url, max_pages=10):
    visited = set() 
    queue = [seed_url]

    os.makedirs("data/pages", exist_ok=True)
    os.makedirs("data/metadata", exist_ok=True)
    
    while queue and len(visited) < max_pages:
        url = queue.pop(0)
        normalized_url = urldefrag(url)[0]
        if normalized_url in visited:
            continue
        if any(normalized_url.lower().endswith(ext) for ext in [".jpg", ".css", ".png", ".webp", ".pdf", ".js", ".php"]):
            continue

        try:
            print(f"Crawling: {normalized_url}")
            html = requests.get(normalized_url, timeout=5).text
            soup = BeautifulSoup(html, 'html.parser')
            with open(f"data/pages/{len(visited)}.html", 'w', encoding='utf-8') as f:
                f.write(soup.get_text())
            with open(f"data/metadata/{len(visited)}.json", "w", encoding='utf-8') as f:
                title = soup.title.string if soup.title else "No title"
                snippet = soup.get_text(strip=True)[:200]
                metadata = {
                    "title" : title,
                    "url" : normalized_url,
                    "snippet" : snippet
                }
                json.dump(metadata, f)
            visited.add(normalized_url)
            links = [urljoin(normalized_url, a['href']) for a in soup.find_all('a', href=True)]
            for link in links:
                norm_link = urldefrag(link)[0]
                if norm_link not in visited and norm_link not in queue:
                    queue.append(norm_link)
            
            time.sleep(1)
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    crawl("https://en.wikipedia.org/wiki/Web_crawler", max_pages=1000)
