import chromadb

CHROMA_DIR = "vector_db"
COLLECTION_NAME = "soc_knowledge_base"

client = chromadb.PersistentClient(path=CHROMA_DIR)

collection = client.get_collection(
    name=COLLECTION_NAME
)

question = input("Question: ")

results = collection.query(
    query_texts=[question],
    n_results=3
)

print("\n===== TOP MATCHES =====\n")

for i, doc in enumerate(results["documents"][0], start=1):
    print(f"\n--- Match {i} ---\n")
    print(doc[:1000])
