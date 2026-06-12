def chunk_text(text, chunk_size=900, overlap=150):
    chunks = []

    start = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]

        if chunk.strip():
            chunks.append(chunk.strip())

        start = end - overlap

    return chunks


def chunk_documents(documents):
    chunked_documents = []

    for doc in documents:
        chunks = chunk_text(doc["content"])

        for index, chunk in enumerate(chunks):
            chunked_documents.append({
                "id": f"{doc['source']}::chunk-{index}",
                "source": doc["source"],
                "chunk_index": index,
                "content": chunk
            })

    return chunked_documents
