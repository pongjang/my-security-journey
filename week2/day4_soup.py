import requests
from bs4 import BeautifulSoup  # 1. 뷰티풀수프 도구 가져오기

# 타겟 설정 (네이버 검색)
target_url = "https://search.naver.com/search.naver"
search_term = "인공지능 보안"
payload = {"query": search_term}
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"}

# 접속 시도
response = requests.get(target_url, headers=header, params=payload)

if response.status_code == 200:
    # 2. 수프 끓이기 (HTML 덩어리를 분석 가능한 상태로 변환)
    # 'html.parser'는 파이썬에 기본 내장된 번역기입니다.
    soup = BeautifulSoup(response.text, "html.parser")

    # 3. 데이터 건져내기 (Parsing)
    # HTML에는 문서의 제목을 담는 <title> 이라는 태그가 무조건 있습니다.
    # select_one("title") -> <title> 태그를 하나 찾아줘!
    # .text -> 태그 껍질(HTML)은 버리고 알맹이 글자만 줘!
    title_text = soup.select_one("title").text

    print("-" * 30)
    print(f"검색어: {search_term}")
    print(f"페이지 제목: {title_text}")
    print("-" * 30)

else:
    print("Fail...")