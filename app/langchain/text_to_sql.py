from fastapi import APIRouter
from .gemma import call_gemma
from .db_chain import raw_to_insert, sql_from_text
from ..schemas import User


# text-to-sql 라우터 구성
sql = APIRouter(
    prefix="/sql"
)


def gemma(text: str) -> dict:
    result = call_gemma(text)
    return {"message": result}

@sql.post('/sql_from_text', tags=["sql"])
def text_to_sql(text: User):
    result = sql_from_text(text)
    return {'message': result}

