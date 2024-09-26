from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..schemas import RawContent
from .db_chain import add_content_to_db

# text-to-sql 라우터 구성
content = APIRouter(
    prefix="/content"
)

# DB 세션을 가져오는 종속성
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 키워드 추출 라우터
@content.post("/keyword", tags=["content"])
def extract_keyword(content: RawContent, db: Session = Depends(get_db)):
    """
    게시물 텍스트를 입력받아 키워드를 추출하고 데이터베이스에 저장 엔드포인트
    """
    result = add_content_to_db(content, db)
    return {"message": "키워드 추출 성공", 
            "data": result
            }