from dotenv import load_dotenv
from ingestion import pdf_loader, chunker
from embeddings.embedder import Embedder
from vectorstore.vectordb import VectorDB
from retrieval.retriever import Retriever
from llm.generator import Generator

load_dotenv()

if __name__ == '__main__':
    #Load PDF
    text = pdf_loader.load_pdf("data/sample.pdf")
    
    #Create chunks
    chunks = chunker.chunk_text(text)

    #Create embeddings
    embedder = Embedder()
    embeddings = [embedder.embed_text(chunk) for chunk in chunks]

    #Store in FAISS
    vectordb = VectorDB(embedding_dim=len(embeddings[0]))
    vectordb.add(embeddings, chunks)

    #LLM Generation
    retriever = Retriever(embedder, vectordb)
    generator = Generator()

    query = input("Ask a question: ")
    context_chunks = retriever.retrieve(query)
    answer = generator.generate(query, context_chunks)
    print("\nAnswer:\n", answer)

    