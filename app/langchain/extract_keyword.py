from fastapi import APIRouter
from .gemma import call_gemma
from .db_chain import raw_to_insert, sql_from_text
from ..schemas import RawContent, User

# text-to-sql 라우터 구성
sql = APIRouter(
    prefix="/content"
)


# TODO: 이후 작성
@sql.post("/raw_to_insert", tags=["content"])
def raw_to_insert(raw: RawContent):
    result = raw_to_insert(raw)
    return {'message': result}