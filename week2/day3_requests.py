import requests

# 1. 주소 변경: 메인 페이지가 아니라 '검색 엔진' 주소로 바꿉니다.
# (원래 주소: https://search.naver.com/search.naver?query=파이썬)
target_url = "https://search.naver.com/search.naver"

# 2. 검색어 준비 (Payload)
# 주소창의 '?query=파이썬' 부분을 딕셔너리로 만듭니다.
search_term = "인공지능 보안"  
payload = {
    "query": search_term
}

# 3. 가면(User-Agent) 준비
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
}

# 4. 접속 시도 (params 옵션 추가!)
# 해석: target_url에 접속하되, header(가면)를 쓰고, payload(검색어)를 들고 가라.
response = requests.get(target_url, headers=header, params=payload)

if response.status_code == 200:
    print(f"Complete!! '{search_term}' 검색 결과 페이지를 가져왔습니다.")
    # 결과가 너무 기니까 앞부분 500자만 확인해 봅니다.
    print("-" * 30)
    print(response.text[:500]) 
else:
    print(f"Fail... Code: {response.status_code}")