from .gemma import call_gemma # gemma 설정 함수
from .utils import get_database_schema # 데이터베이스 정보 반환 함수
from ..schemas import RawContent
from ..crud import create_news
from sqlalchemy.orm import Session
import json


"""
text-to-sql 기능 함수
1. 데이터베이스 스키마 탐색 
2. gemma2:2b 모델 이용한 텍스트를 SQL로 변환
"""
def sql_from_text(user_input):

    # 데이터베이스 스키마 가져오기(반환값)
    schema_info = get_database_schema()
    print("get_databse_schema 성공")


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
    print("call_gemma 실행 전")
    sql_query = call_gemma(prompt)
    print("call_gemma 실행 완료")

    return sql_query



"""
1. 게시물 텍스트에서 키워드를 추출하는 함수
2. Gemma2:2b를 호출하여 텍스트에서 데이터베이스 필드인 title, main_category, sub_category, contents 추출
"""
def extract_keywords_from_text(text: str) -> dict:

    prompt = f"다음 텍스트에서 제목, 메인 카테고리, 서브 카테고리, 내용을 추출하세요: {text}"
    response = call_gemma(prompt)

    try:
        # Gemma2:2b가 JSON 문자열을 반환
        response_json = json.loads(response)
    except json.JSONDecodeError:
        # JSON 파싱이 실패
        print("응답을 JSON으로 변환 불가능:", response)
        raise

    # 응답을 처리하여 필요한 필드로 나눕니다.
    extracted_data = {
        "title": response_json.get("title", ""),
        "main_category": response_json.get("main_category", ""),
        "sub_category": response_json.get("sub_category", ""),
        "contents": response_json.get("contents", "")
    }
    return extracted_data


"""
1. 텍스트에서 키워드를 추출 및 데이터베이스에 삽입하는 함수
"""
def add_content_to_db(content: RawContent, db: Session):
    
    # 키워드 추출
    extracted_data = extract_keywords_from_text(content.contents)
    
    # 데이터베이스에 저장할 데이터 생성
    news_data = {
        "title": extracted_data["title"],
        "main_category": extracted_data["main_category"],
        "sub_category": extracted_data["sub_category"],
        "contents": extracted_data["contents"],
        "source_site": content.source_site
    }

    # 데이터베이스에 삽입
    return create_news(db, news=news_data)