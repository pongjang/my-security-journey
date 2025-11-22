import requests

# 1. 타겟 URL (네이버 검색 엔진)
# 뒤에 ?query=... 부분은 뺍니다. requests가 알아서 붙여줍니다.
url = "https://search.naver.com/search.naver"

# 2. 해커의 검색어 (Payload)
# 딕셔너리 형태로 데이터를 준비합니다.
search_payload = {
    'query': '정보보안',  # 검색어
    'where': 'nexearch'   # 통합검색 탭
}

# 3. 가짜 신분증 (필수)
fake_header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

print(f"검색어 '{search_payload['query']}'(으)로 검색을 시도합니다...")

# 4. params 옵션 사용 (여기가 핵심!)
# url 뒤에 자동으로 ?query=정보보안&where=nexearch 를 붙여서 날려줍니다.
response = requests.get(url, headers=fake_header, params=search_payload)

if response.status_code == 200:
    print("검색 성공!")
    # 실제로 날라간 URL 확인 (우리가 의도한 대로 조립됐는지 확인)
    print(f"최종 공격 URL: {response.url}")
    
    # 결과 페이지 내용에 검색어가 있는지 검증
    if "정보보안" in response.text:
        print("검증 완료: 결과 페이지에 우리가 원한 단어가 포함되어 있습니다.")
else:
    print("검색 실패")