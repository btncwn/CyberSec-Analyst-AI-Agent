from chunk_documents import chunk_documents
from load_documents import load_documents
import chromadb

CHROMA_DIR = "vector_db"
COLLECTION_NAME = "soc_knowledge_base"


def main():
    client = chromadb.PersistentClient(path=CHROMA_DIR)

    try:
        client.delete_collection(name=COLLECTION_NAME)
    except Exception:
        pass

    collection = client.get_or_create_collection(
        name=COLLECTION_NAME
    )

    documents = load_documents()
    documents = chunk_documents(documents)

    if not documents:
        print("No markdown documents found.")
        return

    collection.add(
        ids=[doc["id"] for doc in documents],
documents=[doc["content"] for doc in documents],
metadatas=[
    {
        "source": doc["source"],
        "chunk_index": doc["chunk_index"]
    }
    for doc in documents
]
    )

    print(f"Ingested {len(documents)} documents into ChromaDB.")


if __name__ == "__main__":
    main()
