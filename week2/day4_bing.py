import requests
from bs4 import BeautifulSoup

# 1. 타겟: Bing 글로벌 검색
target_url = "https://www.bing.com/search"

search_term = "Artificial Intelligence Security"
# Bing은 검색어 파라미터 이름이 'q'입니다.
payload = {"q": search_term}

# 2. 가면(Header): 영어 사용자(en-US)인 척 위장
header = {
    # 기존 header 지우고 이걸로 교체하세요!

    # 1. 신분증 (브라우저 정보)
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    
    # 2. 언어 설정 (영어)
    "Accept-Language": "en-US,en;q=0.9",
    
    # 3. [핵심] "나 구글에서 링크 타고 왔어!" (의심을 피하는 기술)
    "Referer": "https://www.google.com/",
    
    # 4. "나 이미지도 받을 수 있고, 텍스트도 받을 수 있어" (브라우저 흉내)
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
    
    # 5. 보안 연결 요청
    "Upgrade-Insecure-Requests": "1"
}


# 3. 접속 시도
response = requests.get(target_url, headers=header, params=payload)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    # 4. Bing의 검색 결과 제목 찾기 (li.b_algo 안의 h2 태그)
    bing_results = soup.select("li.b_algo h2")

    print(f"Bing US Results for '{search_term}':\n")

    for result in bing_results:
        title = result.text
        # 링크 가져오기
        link_tag = result.select_one("a")
        # 링크가 있으면 가져오고, 없으면 "No Link"라고 표시
        link = link_tag['href'] if link_tag else "No Link"

        print(f"Title: {title}")
        print(f"Link: {link}")
        print("-" * 10)
    # (위의 for문이 끝난 뒤, else 바로 위에 추가)
    
    # for문 밖으로 나와서(들여쓰기 주의!) 저장 코드를 씁니다.
    with open("bing_debug.html", "w", encoding="utf-8") as f:
        f.write(response.text)
    print("bing_debug.html 파일이 생성되었습니다. 열어서 확인해보세요!")

else:
    print(f"Blocked... Code: {response.status_code}")