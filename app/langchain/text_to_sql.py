from fastapi import APIRouter
from .gemma import call_gemma
from ..schemas import RawContent


# text-to-sql 라우터 구성
sql = APIRouter(
    prefix="/sql"
)

# 라우터 테스트
@sql.get("/test", tags=["sql"])
def text_to_sql(text: str) -> dict:
    result = call_gemma(text)
    return {"message": result}

@sql.post('/raw_to_insert', tags=["sql"])
def raw_to_insert(raw: RawContent):
    result = raw_to_insert(raw)
    return ""