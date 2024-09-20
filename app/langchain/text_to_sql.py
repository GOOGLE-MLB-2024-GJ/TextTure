from fastapi import APIRouter

# text-to-sql 라우터 구성 : v1은 임시 prefix
sql = APIRouter(
    prefix="/v1"
)

# 라우터 테스트
@sql.get("/test", tags=["sql"])
async def text_to_sql():
    return {"message" : "hi"}