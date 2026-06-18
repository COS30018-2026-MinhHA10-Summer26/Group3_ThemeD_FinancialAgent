import requests
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from ai_integration.models.llm import get_llm
import os

API_KEY = load_dotenv() and os.getenv("API_KEY")
query = "NVIDIA annual reports 2024"
processed_query = f"{query}:pdf"
response = requests.get("https://serpapi.com/search", params={
    "q": query,
    "api_key": API_KEY,
    "num": 3
})

data = response.json()
for result in data.get("organic_results", []):
    print(result["title"])
    print(result["link"])
    try: 
        pdf_response = requests.get(result["link"])
        pdf_response.raise_for_status()
        with open(f"ai_integration/data/raw/{query}_{result['title']}.pdf", "wb") as f:
            f.write(pdf_response.content)

        print("Successfully extracted text from PDF.")
    except Exception as e:
        print(f"Error processing PDF: {e}")
