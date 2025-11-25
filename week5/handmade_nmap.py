#내가 한것
import requests

target_url = "http://testphp.vulnweb.com/login.php"
payload = {'uname':'admin', 'pass':'admin'}

print(f"[{target_url}]의 접속을 시작합니다...")

requests.post(url=target_url, data=payload)
response = requests.post(url=target_url, data=payload)
res = response
print(res.text)

#gemini가 한것
import requests

# 타겟 설정 (로그인 처리 페이지)
# 주의: 실제 form action은 userinfo.php로 넘어가는 경우가 많지만, 연습이니 login.php로 시도해봅니다.
target_url = "http://testphp.vulnweb.com/userinfo.php" 

# 공격 payload (아이디/비번)
payload = {'uname': 'test', 'pass': 'test'} 
# ('test'/'test'는 이 사이트의 또 다른 유효한 계정입니다. admin/admin이 안 될 수도 있어서 변경했습니다)

print(f"[{target_url}]에 로그인을 시도합니다...")

# 요청 전송 및 응답 저장
res = requests.post(url=target_url, data=payload)

# [핵심] 결과 판단 로직 (Parsing)
# 응답받은 HTML 문서 안에 'Logout'이라는 단어가 있는지 확인
if "Logout" in res.text:
    print("---------------------------------------")
    print("[★] 로그인 성공! (Success)")
    print(f"[+] 사용한 계정: {payload['uname']} / {payload['pass']}")
    print("---------------------------------------")
else:
    print("---------------------------------------")
    print("[!] 로그인 실패... (Failed)")
    print("---------------------------------------")

# (참고용) 실제 응답 코드의 일부만 출력해서 확인
print("\n[서버 응답 맛보기]:")
print(res.text[:300]) # 앞 300글자만 출력