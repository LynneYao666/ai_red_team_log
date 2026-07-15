from langchain_ollama import OllamaLLM 
llm = OllamaLLM(model="llama3:8b")

question = "What is prompt injection in the context of LLM security? Answer is 2 sentences. "
response = llm.invoke(question) 

print("Question:", question)
print("Response:", response) 

