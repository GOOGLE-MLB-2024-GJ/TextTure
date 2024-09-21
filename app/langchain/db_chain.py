from .gemma import call_gemma # gemma 설정 함수
from .utils import get_database_schema # 데이터베이스 정보 반환 함수
from ..schemas import RawContent

"""
text-to-sql 기능 함수
1. 데이터베이스 스키마 탐색 
2. gemma2:2b 모델 이용한 텍스트를 SQL로 변환
"""
def sql_from_text(user_input: str) -> str:

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

    위 스키마를 참고하여 다음 요청을 SQL 쿼리로 변환하세요, 단 SQL 쿼리 외에 부가적인 설명을 붙이지 않아야 합니다.:

    {user_input}
    """

    # gemma2:2b 모델: SQL 생성
    sql_query = call_gemma(prompt)

    return sql_query


def raw_to_insert(raw:RawContent):
    return ""