from fastapi import FastAPI
from .langchain.text_to_sql import sql

app = FastAPI()

# text-to-sql 라우터 설정
app.include_router(sql)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
