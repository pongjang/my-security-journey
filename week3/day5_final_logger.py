import requests
import time
from datetime import datetime

url ="https://httpbin.org/get"

keywords = ["정보보안", "Python", "Hacking", "Gemini_pro"]

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

print("===자동화 기록 시스템 가동===\n")

for word in keywords:
    try:
        response = requests.get(url, headers=headers, params={'q': word})

        if response.status_code == 200:
            print(f"[+] 성공: {word}")
            with open("hacking_log.txt", "a", encoding="utf-8") as f:
                now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                log_message = f"[{now}]검색어 '{word}' 전송성공 (URL:{response.url})\n"
                f.write(log_message)

        else:
            print(f"[-] 실패: {response.status_code}")
    
    except Exception as e:
        print(f"[!] 에러발생: {e}")
    time.sleep(1)
print("\n===모든작업 완료. 'hacking_log.txt' 파일을 확인하세요===")