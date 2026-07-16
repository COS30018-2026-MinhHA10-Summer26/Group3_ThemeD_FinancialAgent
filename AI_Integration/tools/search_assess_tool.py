from transformers import AutoTokenizer
import torch

tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")


def similarity_score(query, documents):
    if not documents:
        return 0.0

    query_encoding = tokenizer(query, return_tensors="pt")
    doc_encodings = [tokenizer(doc, return_tensors="pt") for doc in documents if doc]

    if not doc_encodings:
        return 0.0

    similarities = [
        torch.cosine_similarity(query_encoding["input_ids"], doc_encoding["input_ids"], dim=1).item()
        for doc_encoding in doc_encodings
    ]
    return max(similarities) if similarities else 0.0


def calculate_coverage(query, documents: list[str]) -> float:
    return similarity_score(query, documents)
