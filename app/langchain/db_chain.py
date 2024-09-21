# from langchain.utilities import SQLDatabase
# from langchain_experimental.sql import SQLDatabaseChain
# from gemma import llm
from dotenv import load_dotenv
import os

# 새로 생성 : 경준
from .gemma import call_gemma # gemma 설정 함수
from .utils import get_database_schema # 데이터베이스 정보 반환 함수

load_dotenv(dotenv_path='../../.env.development')

MARIADB_ROOT_PASSWORD = os.getenv('MARIADB_ROOT_PASSWORD')
MARIADB_DATABASE = os.getenv('MARIADB_DATABASE')

SQLALCHEMY_DATABASE_URL = f'mysql+pymysql://root:{MARIADB_ROOT_PASSWORD}@localhost:3306/{MARIADB_DATABASE}'

# db = SQLDatabase.from_uri(SQLALCHEMY_DATABASE_URL, sample_rows_in_table_info=2)
# db_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True)


"""
text-to-sql 기능 함수
1. 데이터베이스 스키마 탐색 
2. gemma2:2b 모델 이용한 텍스트를 SQL로 변환
"""
def sql_from_text(user_input):

    # 데이터베이스 스키마 가져오기(반환값)
    schema_info = get_database_schema()


    """
    1. schema_str 정리
    - 기존 shcema_info(예시)
    schema_info = {
    "users": ["id", "name", "email"],
    }

    - 변경 후 schema_str
    "Table users: id, name, email\n

    2. 프롬프트 작성(성능 올리기 위해서 추가적인 작성 필요)
    """
    
    schema_str = "\n".join([f"Table {table}: {', '.join(columns)}" for table, columns in schema_info.items()])
    prompt = f"""
    다음은 데이터베이스 스키마입니다:

    {schema_str}

    위 스키마를 참고하여 다음 요청을 SQL 쿼리로 변환하세요:

    {user_input}
    """

    # gemma2:2b 모델: SQL 생성
    sql_query = call_gemma(prompt)

    return sql_query