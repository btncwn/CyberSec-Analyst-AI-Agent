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

    if not documents:
        print("No markdown documents found.")
        return

    collection.add(
        ids=[doc["source"] for doc in documents],
        documents=[doc["content"] for doc in documents],
        metadatas=[{"source": doc["source"]} for doc in documents]
    )

    print(f"Ingested {len(documents)} documents into ChromaDB.")


if __name__ == "__main__":
    main()
