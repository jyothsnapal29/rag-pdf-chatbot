# RAG PDF Chatbot

A **Retrieval-Augmented Generation (RAG)** system that allows you to ask questions about PDF documents using embeddings and vector search.

---

## Features

- Extract text from PDF documents  
- Intelligent chunking with overlap  
- Generate embeddings (OpenAI / mock)  
- Fast similarity search using FAISS  
- Modular and scalable architecture  
- Retrieve relevant document context  

---

## Architecture
PDF → Chunk → Embed → Store (FAISS)

User Query → Embed → Retrieve → Relevant Chunks


---

## Project Structure
```
chat-with-pdfs/
│
├── src/
│ ├── main.py
│
│ ├── config/
│ │ └── config.py
│
│ ├── ingestion/
│ │ ├── pdf_loader.py
│ │ └── chunker.py
│
│ ├── embeddings/
│ │ └── embedder.py
│
│ ├── vectorstore/
│ │ └── vectordb.py
│
│ ├── retrieval/
│ │ └── retriever.py
│
│ └── utils/
│ └── logger.py
│
├── data/
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Setup

### 1. Clone the repository

git clone https://github.com/YOUR_USERNAME/rag-pdf-chatbot.git
cd rag-pdf-chatbot

### 2. Create and activate virtual environment

python -m venv ai-env
source ai-env/bin/activate

### 3. Install dependencies

pip install -r requirements.txt

### 4. Configure environment variables

Create a .env file in the root directory:
OPENAI_API_KEY=your_api_key_here

### 5. Run the Project

python src/main.py

Example Query
What is the main topic of the document?

---

### Tech Stack
```
Python
OpenAI API (Embeddings)
FAISS (Vector Database)
NumPy
PyPDF
```

---

## Author

**Jyothsna Pal**

Aspiring AI Engineer | GenAI Developer | Building real-world AI systems

---