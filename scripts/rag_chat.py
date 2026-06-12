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

print("\n===== RAW OLLAMA RESPONSE =====\n")
print(response.status_code)
print(response.text)

print("\n===== ANSWER =====\n")

data = response.json()

if "response" in data:
    print(data["response"])
else:
    print("Ollama did not return a response field.")
    print(data)
