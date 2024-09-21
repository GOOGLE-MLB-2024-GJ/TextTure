"""
db_chain.py 등 스크립트 내의 메서드(함수)에 사용되는 함수를 정의한 스크립트
"""
from sqlalchemy import inspect
from database import SessionLocal


"""
데이터베이스 스키마(테이블 및 컬럼 정보) 반환 함수
"""
def get_database_schema():

    # 데이터베이스 연결
    db = SessionLocal()
    
    # 데이터베이스 메타데이터 확인
    inspector = inspect(db.bind)  

    # 데이터베이스 정보 담기
    schema_info = {}
    
    # 데이터베이스의 모든 테이블과 컬럼 정보 가져오기
    for table_name in inspector.get_table_names():
        columns = inspector.get_columns(table_name)
        column_names = [column["name"] for column in columns]
        schema_info[table_name] = column_names

    db.close()
    
    return schema_info
