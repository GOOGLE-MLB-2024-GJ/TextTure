from fastapi import FastAPI
from .langchain.text_to_sql import sql
from .langchain.extract_keyword import content
from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# text-to-sql 라우터 설정
app.include_router(sql)

# extract-keyword 라우터 설정
app.include_router(content)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}