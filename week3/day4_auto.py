import requests
import time

# 1. 타겟 변경: 해킹/개발 연습 전용 사이트 (httpbin)
# /get 엔드포인트는 우리가 보낸 데이터를 그대로 돌려줍니다.
url = "https://httpbin.org/get"

# 2. 검색어(공격 패턴) 리스트
keywords = ["정보보안", "AI 해킹", "Python requests", "파이썬 독학", "Gemini"]

# 3. 가짜 헤더
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

print(f"총 {len(keywords)}개의 데이터 전송 테스트를 시작합니다...\n")

for word in keywords:
    # httpbin에 데이터를 보낼 때는 params에 담아서 보냅니다.
    payload = {'target_word': word, 'id': 'admin'} 
    
    try:
        response = requests.get(url, headers=headers, params=payload)
        
        # httpbin은 웬만하면 200 OK를 줍니다.
        if response.status_code == 200:
            print(f"[성공] 데이터: '{word}' -> 전송 확인됨")
            
            # httpbin이 돌려준 응답(JSON)에서 우리가 보낸 값이 잘 들어갔는지 확인
            # response.json()은 서버의 응답을 파이썬 딕셔너리로 바꿔줍니다.
            args = response.json()['args']
            print(f"       서버가 인식한 값: {args}")
            
        else:
            print(f"[실패] 상태 코드: {response.status_code}")
            
    except Exception as e:
        print(f"[에러] {e}")
        
    time.sleep(1)

print("\n모든 작업이 완료되었습니다.")