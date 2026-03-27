import numpy
import faiss

class VectorDB:
    def __init__(self, embedding_dim):
        self.embedding_dim = embedding_dim
        self.index = faiss.IndexFlatL2(self.embedding_dim)
        self.texts = []

    def add(self, embeddings, texts):
        self.index.add(numpy.array(embeddings).astype("float32" ))
        self.texts.extend(texts)

    def query(self, embedding, top_k = 3):
        distance, index = self.index.search(numpy.array([embedding]).astype("float32"), top_k)
        return [self.texts[idx] for idx in index[0]]