from pydoc import text

from openai import OpenAI
import random

class Embedder:
    def __init__(self, model_name="text-embedding-3-small"):    
        self.client = OpenAI()
        self.model_name = model_name

    def embed_text(self, chunk:str):
        response = self.client.embeddings.create(
            model=self.model_name, 
            input=chunk
        )
        return response.data[0].embedding
