def chunk_text(text:str, chunk_size = 500, overlap=50):
    start = 0
    chunks = []

    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start+= chunk_size - overlap
        
    return chunks