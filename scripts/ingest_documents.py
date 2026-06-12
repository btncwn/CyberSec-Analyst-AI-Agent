from pathlib import Path
import chromadb

KNOWLEDGE_BASE_DIR = Path("knowledge_base")
CHROMA_DIR = "vector_db"
COLLECTION_NAME = "soc_knowledge_base"


def read_markdown_files():
    documents = []

    for file_path in KNOWLEDGE_BASE_DIR.rglob("*.md"):
        text = file_path.read_text(encoding="utf-8")

        documents.append({
            "id": str(file_path),
            "text": text,
            "source": str(file_path)
        })

    return documents


def main():
    client = chromadb.PersistentClient(path=CHROMA_DIR)

    collection = client.get_or_create_collection(
        name=COLLECTION_NAME
    )

    documents = read_markdown_files()

    if not documents:
        print("No markdown documents found in knowledge_base/")
        return

    collection.add(
        ids=[doc["id"] for doc in documents],
        documents=[doc["text"] for doc in documents],
        metadatas=[{"source": doc["source"]} for doc in documents]
    )

    print(f"Ingested {len(documents)} documents into ChromaDB.")


if __name__ == "__main__":
    main()
