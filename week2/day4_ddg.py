import requests
from bs4 import BeautifulSoup

# 타겟: DuckDuckGo HTML 버전
target_url = "https://html.duckduckgo.com/html/"
search_term = "Artificial Intelligence Security"
payload = {"q": search_term}
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"}

print(f"🔍 '{search_term}' 데이터 수집 시작...")

response = requests.post(target_url, headers=header, data=payload)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    results = soup.select("a.result__a")

    # [핵심] 파일로 저장하기 (Day 2 + Day 4 융합)
    # 'ai_security_news.csv' 라는 이름으로 저장합니다.
    # CSV는 쉼표(,)로 데이터를 구분하는 파일로, 엑셀에서 열립니다.
    filename = "ai_security_news.csv"
    
    with open(filename, "w", encoding="utf-8") as f:
        # 1. 맨 윗줄에 제목(헤더) 적기
        f.write("제목,링크\n")
        
        count = 0
        for result in results:
            title = result.text
            link = result['href']
            
            # 2. 콤마(,)로 구분해서 파일에 쓰기
            # 제목에 콤마가 있으면 꼬일 수 있어서 콤마를 제거(.replace)해주는 센스!
            clean_title = title.replace(",", " ") 
            f.write(f"{clean_title},{link}\n")
            
            count += 1
            
    print(f"✅ 수집 완료! 총 {count}개의 기사가 '{filename}'에 저장되었습니다.")

else:
    print(f"❌ 접속 실패... Code: {response.status_code}")