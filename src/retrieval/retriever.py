from embeddings.embedder import Embedder
from vectorstore.vectordb import VectorDB

class Retriever:
    def __init__(self, embedder, vectordb):
        self.embedder = embedder
        self.vectordb = vectordb

    def retrieve(self, query:str, top_k=3):
        query_embedding = self.embedder.embed_text(query)
        results = self.vectordb.query(query_embedding, top_k)
        return results