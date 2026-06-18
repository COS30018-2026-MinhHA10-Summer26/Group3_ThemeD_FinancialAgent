from transformers import AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
import torch

def similarity_score(query, documents):
    query_encoding = tokenizer(query, return_tensors="pt")
    doc_encodings = [tokenizer(doc, return_tensors="pt") for doc in documents]
    return max([torch.cosine_similarity(query_encoding['input_ids'], doc_encoding['input_ids'], dim=1).item() for doc_encoding in doc_encodings])

def calculate_coverage(query, documents: list[str])-> float:
        return similarity_score(query, documents) 
