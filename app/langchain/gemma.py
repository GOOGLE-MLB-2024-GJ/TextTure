from langchain_community.llms import Ollama
llm = Ollama(model="gemma2:2b")
response = llm.invoke("how are you today?")
