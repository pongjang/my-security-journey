import requests
from bs4 import BeautifulSoup

# 1. 타겟 변경: 구글 검색
target_url = "https://www.google.com/search"

# 2. 검색어: 영어로 'Artificial Intelligence Security' 검색
search_term = "Artificial Intelligence Security"
payload = {"q": search_term} # 구글은 파라미터 이름이 'query'가 아니라 'q'입니다.

# 3. [핵심] 가면(Header) 업그레이드
# Accept-Language: "en-US" -> "나 미국 영어 쓰는 사람이야" 라고 선언
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9" 
}

response = requests.get(target_url, headers=header, params=payload)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    # 4. 구글의 제목 찾기
    # 구글은 클래스 이름이 매번 바뀌어서 어렵습니다.
    # 하지만 보통 검색 결과 제목은 <h3> 태그를 씁니다.
    google_titles = soup.select("h3")

    print(f"Google US Results for '{search_term}':\n")

    for title in google_titles:
        # 제목 글자가 비어있는 경우도 있어서 필터링
        if title.text:
            print(f"제목: {title.text}")
            # 구글은 링크 찾기가 조금 더 복잡해서 일단 제목만 뽑아봅니다.
            print("-" * 10)
    # (위의 for문이 끝난 뒤, else 위쪽에 추가)
    
    # 구글이 보낸 진짜 내용을 파일로 저장해서 확인해 봅시다.
    with open("google_debug.html", "w", encoding="utf-8") as f:
        f.write(response.text)
    print("google_debug.html 파일이 생성되었습니다. 열어서 확인해보세요!")

else:
    print(f"Google blocked us... Code: {response.status_code}")