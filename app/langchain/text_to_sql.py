from fastapi import APIRouter, HTTPException
from schemas import User
from .db_chain import sql_from_text

# text-to-sql 라우터 구성
sql = APIRouter(
    prefix="/sql"
)

# 라우터 테스트
@sql.get("/test", tags=["sql"])
async def text_to_sql_test():
    return {"message" : "hi"}


# text-to-sql API
@sql.post("/text", tags=["sql"])
async def text_to_sql(user_input: User):

    # text-to-sql 기능 함수 실행
    try:
        sql_query = sql_from_text(user_input.user_input)
        return {"response": sql_query}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"SQL 변환 중 오류 발생: {e}")

