from googlesearch import search
from bs4 import BeautifulSoup
import requests
from typing import Any

# query = "Download NVIDIA annual reports from the official company website for 2024"
# processed_query = query.replace(" ", "+")
# results = requests.get(f"https://www.google.com/search?q={processed_query}&num=5")
# print(f"{results.status_code} {results.reason}")

# for result in results:
#     print(result)
import requests

query = "NVIDIA annual reports 2024"
response = requests.get("https://api.duckduckgo.com/", params={
    'q': query,
    'format': 'json'
})

if response.status_code == 200:
    data = response.json()
    print("DuckDuckGo Results:")
    for i, result in enumerate(data.get('Results', [])[:5], 1):
        print(f"{i}. {result.get('Title')}: {result.get('FirstURL')}")