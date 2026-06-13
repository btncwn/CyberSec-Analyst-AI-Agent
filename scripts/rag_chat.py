import chromadb
import requests
import json
import sys
import time

CHROMA_DIR = "vector_db"
COLLECTION_NAME = "soc_knowledge_base"
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "qwen3:8b"

def get_ollama_response(prompt, max_tokens=400):
    """Get response from Ollama with robust error handling"""
    try:
        print(f"  [Sending request to Ollama with max_tokens={max_tokens}]")
        
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL,
                "prompt": prompt,
                "stream": False,
                "options": {
                    "num_predict": max_tokens,  # Use parameter
                    "temperature": 0.2,
                    "top_p": 0.9,
                    "stop": ["\n\n\n", "Context:", "CONTEXT:"]  # Stop at natural breaks
                }
            },
            timeout=120
        )
        
        print(f"  [Response status: {response.status_code}]")
        response.raise_for_status()
        
        result = response.json()
        answer = result.get("response", "").strip()
        
        if not answer:
            print("  [Warning: Empty response from Ollama]")
            return None
            
        print(f"  [Generated {len(answer)} characters]")
        return answer
        
    except requests.exceptions.Timeout:
        print("\n❌ Timeout: Ollama took too long to respond")
        return None
    except requests.exceptions.ConnectionError:
        print("\n❌ Connection error: Is Ollama running?")
        return None
    except requests.exceptions.RequestException as e:
        print(f"\n❌ Request error: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"\n❌ JSON parse error: {e}")
        return None

def main():
    print("\n=== SOC RAG Assistant ===\n")
    
    # Test Ollama connection first
    try:
        test_response = requests.get("http://localhost:11434/api/tags", timeout=5)
        if test_response.status_code != 200:
            print("❌ Ollama is not responding correctly")
            sys.exit(1)
        print("✓ Ollama connection verified")
    except:
        print("❌ Cannot connect to Ollama. Make sure it's running.")
        sys.exit(1)
    # Connect to database
    try:
        client = chromadb.PersistentClient(path=CHROMA_DIR)
        collection = client.get_collection(name=COLLECTION_NAME)
        print("✓ Database connected")
    except Exception as e:
        print(f"❌ Database error: {e}")
        sys.exit(1)
    # Get question
    question = input("\nQuestion: ").strip()
    if not question:
        print("No question provided")
        sys.exit(1)
    # Search knowledge base
    print("\n🔍 Searching knowledge base...")
    try:
        results = collection.query(
            query_texts=[question],
            n_results=3,
            include=["documents", "metadatas"]
        )

        print("\nRetrieved documents:")
        for meta in results["metadatas"][0]:
            print(meta.get("source"))

    except Exception as e:
        print(f"❌ Search error: {e}")
        sys.exit(1)
    
    if not results["documents"][0]:
        print("❌ No relevant context found")
        sys.exit(1)
    
    print(f"✓ Found {len(results['documents'][0])} relevant documents")
    
    # Prepare context
    context = "\n\n---\n\n".join(results["documents"][0])
    context_size = len(context)
    print(f"  Context size: {context_size} characters")
    
    # Adjust max_tokens based on context size
    max_tokens = 400  # Default
    if context_size < 500:
        max_tokens = 300  # Smaller context = shorter answer
    elif context_size > 2000:
        max_tokens = 600  # Larger context might need more tokens
    
    prompt = f"""Answer based ONLY on this context. Be direct and concise:

CONTEXT:
{context}

QUESTION: {question}

ANSWER:"""
    
    print("\n🤔 Generating answer...\n")
    print("="*50)
    
    start_time = time.time()
    answer = get_ollama_response(prompt, max_tokens=max_tokens)
    elapsed = time.time() - start_time
    
    if answer:
        print(f"\n{answer}")
        print("\n" + "="*50)
        print(f"\n⏱️  Response time: {elapsed:.1f} seconds")
        print(f"📝 Answer length: {len(answer)} characters")
    else:
        print("\n❌ Failed to generate answer")
        print("\nTroubleshooting tips:")
        print("  1. Check if Ollama is running: curl http://localhost:11434/api/tags")
        print("  2. Try a different model: Change MODEL to 'llama3.2:3b'")
        print("  3. Check Ollama logs for errors")
        print("  4. Restart Ollama: killall ollama && ollama serve")
        sys.exit(1)
    
    # Show sources
    print("\n📚 SOURCES:\n")
    seen = set()
    for meta in results["metadatas"][0]:
        source = meta.get('source', 'Unknown')
        if source not in seen:
            print(f"  • {source}")
            seen.add(source)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Interrupted by user")
        sys.exit(0)
