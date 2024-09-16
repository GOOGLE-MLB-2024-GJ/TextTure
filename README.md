# TextTure(Text to Structured)

## Introduction

The TextTure project aims to automatically convert unstructured text data into structured data so that it can be easily stored in a database.
The main goal is to have the Gemma 2B model analyze unstructured text data such as message board posts or comments written by users, categorize it into a structured format, and match it with database fields.
The project automates and simplifies the task of converting unstructured data into structured data, improving the efficiency of data management.

## Project Execution

```bash
$ docker compose up --build
```

## Gemma2:2b Setup via Ollama in Local

1. [Install Ollama](https://ollama.com/)
2. [Install gemma2:2b](https://ollama.com/library/gemma2:2b)

```bash
ollama run gemma2:2b
```
3. Install dependency

```bash
$ pip install -r requirements.txt
```

3. Now you can chat with your LLM model

```python
from langchain_community.llms import Ollama
llm = Ollama(model="gemma2:2b")
response = llm.invoke("how are you today?")
print(response)
# response: I'm doing well! 😊  How are you today? 
```
