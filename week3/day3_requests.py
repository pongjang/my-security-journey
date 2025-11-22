import requests

url = "https://www.naver.com"

# 1. 가짜 신분증(Header) 만들기
# 이것은 실제 크롬 브라우저가 서버에 보내는 User-Agent 값입니다.
fake_header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

print("브라우저로 위장하여 접속을 시도합니다...")

# 2. headers 옵션을 추가하여 요청 보내기
# (중요: 여기서 headers=fake_header를 안 넣으면 위장이 안 됩니다!)
response = requests.get(url, headers=fake_header)

if response.status_code == 200:
    print("위장 접속 성공!")
    print(f"서버 상태 코드: {response.status_code}")
    
    # 우리가 보낸 헤더가 제대로 적용됐는지 확인 (내 요청 정보 확인)
    print("\n[우리가 보낸 가짜 명함]")
    print(response.request.headers) 
else:
    print("접속 실패/차단됨")