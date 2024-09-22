from fastapi import APIRouter
from .gemma import call_gemma
from .db_chain import raw_to_insert, sql_from_text
from ..schemas import RawContent


# text-to-sql 라우터 구성
sql = APIRouter(
    prefix="/sql"
)


def gemma(text: str) -> dict:
    result = call_gemma(text)
    return {"message": result}

@sql.get('/sql_from_text', tags=["sql"])
def text_to_sql(text:str):
    result = sql_from_text(text)
    return {'message': result}

# TODO: 이후 작성
@sql.post("/raw_to_insert", tags=["sql"])
def raw_to_insert(raw: RawContent):
    result = raw_to_insert(raw)
    return {'message': result}
