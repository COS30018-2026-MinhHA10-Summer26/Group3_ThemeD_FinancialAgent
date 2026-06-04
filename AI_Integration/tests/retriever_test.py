import os
import yaml
from ai_integration.rag.retriever import Retriever


def main():

    config_path = os.path.expanduser("~/financial_agent/ai_integration/config.yaml")
    config = yaml.safe_load(open(config_path))

    retriever = Retriever(config)

    while True:

        query = input("\nEnter query: ")

        results,latency = retriever.retrieve(query)

        print("\nTop Results:\n")

        for i, r in enumerate(results):

            print(f"Result {i+1}")
            print(f"Source: {r['source']} (page {r['page']})")
            print(f"Score: {r['score']}")
            print(r["text"][:300])
            print("-"*50)


if __name__ == "__main__":
    main()