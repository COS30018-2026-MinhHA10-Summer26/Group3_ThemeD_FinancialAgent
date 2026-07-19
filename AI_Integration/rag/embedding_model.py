import os

import numpy as np
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings


load_dotenv()


class EmbeddingModel:

    def __init__(self, model_name):
        openai_key = os.getenv("OPENAI_API_KEY")
        self.model = OpenAIEmbeddings(model=model_name, openai_api_key=openai_key)

    def embed(self, texts):
        return np.asarray(self.model.embed_documents(texts), dtype="float32")
    
    def embed_query(self, query):
        return np.asarray(self.model.embed_query(query), dtype="float32")

    def embed_documents(self, texts):
        return self.embed(texts)

# model = EmbeddingModel("text-embedding-3-small")
# emb = model.embed(["test sentence"])
# print(emb.shape