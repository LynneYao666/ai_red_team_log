import chromadb
from langchain_ollama import OllamaEmbeddings

embeddings = OllamaEmbeddings(model="nomic-embed-text")

documents = [
	"Prompt injection is an attack where malicious input overrides an LLM's original instructions.",
    "The Great Wall of China was built over centuries to protect against invasions.",
    "RAG pipelines combine a retrieval step with a language model to answer questions using external documents.",
    "Cats are popular pets known for their independence and agility.",
    "Indirect prompt injection hides malicious instructions inside documents the model later reads."]

doc_embeddings = embeddings.embed_documents(documents)
print(f'generated {len(doc_embeddings)} vectors, vector dimention: {len(doc_embeddings[0])}')

client = chromadb.Client()
collection = client.create_collection(name = "test_collection")

collection.add(
	embeddings=doc_embeddings,
	documents= documents,
	ids=[f"doc_{i}" for i in range(len(documents))]
)
query = "How do attackers manipulate LLM behavior?"
query_embedding = embeddings.embed_query(query) 

results = collection.query(
	query_embeddings=[query_embedding],
	n_results=3
)

print(f"\ncheck:{query}")
print
