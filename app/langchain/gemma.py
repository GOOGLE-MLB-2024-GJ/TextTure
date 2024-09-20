"""
langchain 프레임워크의 Ollama 클래스를 사용하여 프로젝트에 사용될 gemma2:2b를 설정하는 스크립트
"""

from langchain_community.llms import Ollama

# ollama를 이용한 gemma2:2b 모델 설정
def call_gemma(prompt: str) -> str:
    

    try:
        # Gemma2:2b 모델 설정
        llm = Ollama(model="gemma2:2b")
        # 프롬프트로 모델 호출(invoke 메서드 사용해야지 추가적인 메시지 x)
        response = llm.invoke(prompt)  

        return response
    
    # 예외처리
    except Exception as e:
        print(f"Gemma 모델 호출 오류: {e}")
        return ""


"""
테스트 진행을 위한 코드
아래 주석을 해제한 후 cd로 langchain의 이동한 후 python gemma.py을 
terminal에서 실행하면 답변이 생성
"""
# if __name__ == "__main__":

#     # 테스트 진행
#     prompt = "안녕? 반가워"
#     response = call_gemma(prompt)
    
#     # 응답 출력
#     print(f"Gemma의 응답: {response}")
