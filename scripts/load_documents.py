from pathlib import Path

SEARCH_PATHS = [
    "knowledge_base",
    "external_sources"
]

def load_documents():
    documents = []

    for base_path in SEARCH_PATHS:
        for file_path in Path(base_path).rglob("*.md"):
            documents.append({
                "source": str(file_path),
                "content": file_path.read_text(
                    encoding="utf-8",
                    errors="ignore"
                )
            })

    return documents

if __name__ == "__main__":
    docs = load_documents()

    print(f"\nLoaded {len(docs)} documents\n")

    for doc in docs:
        print(doc["source"])
