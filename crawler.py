import requests, os
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def crawl(seed_url, max_pages=10):
    visited = set() 
    queue = [seed_url]

    os.makedirs("data/pages", exist_ok=True)

    while queue and len(visited) < max_pages:
        url = queue.pop(0)
        if url in visited:
            continue

        try:
            print(f"Crawling: {url}")
            html = requests.get(url, timeout=5).text
            soup = BeautifulSoup(html, 'html.parser')
            with open(f"data/pages/{len(visited)}.html", 'w', encoding='utf-8') as f:
                    f.write(soup.get_text())
            visited.add(url)
            links = [urljoin(url, a['href']) for a in soup.find_all('a', href=True)]
            queue.extend(links)
        except Exception as e:
            print(f"Error: {e}")

