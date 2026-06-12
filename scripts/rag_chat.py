import chromadb
import requests

CHROMA_DIR = "vector_db"
COLLECTION_NAME = "soc_knowledge_base"
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3.2:3b"

client = chromadb.PersistentClient(path=CHROMA_DIR)
collection = client.get_collection(name=COLLECTION_NAME)

question = input("Question: ")

results = collection.query(
    query_texts=[question],
    n_results=3
)

context = "\n\n".join(results["documents"][0])

prompt = f"""
You are a cybersecurity analyst.

Use ONLY the context below.

CONTEXT:
{context}

QUESTION:
{question}
"""

response = requests.post(
    OLLAMA_URL,
    json={
        "model": MODEL,
        "prompt": prompt,
        "stream": False
    }
)

data = response.json()

print("\n===== ANSWER =====\n")

if "response" in data:
    print(data["response"])

    print("\n===== SOURCES USED =====\n")

    sources = []

    for metadata in results["metadatas"][0]:
        source = metadata["source"]

        if source not in sources:
            sources.append(source)

    for source in sources:
        print(f"- {source}")

else:
    print("Ollama Error:")
    print(data)
