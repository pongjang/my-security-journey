import socket
from datetime import datetime

target= input("타겟 IP를 입력하세요")

print("-" * 50)
print(f"타겟 스캔 시작: {target}")
print(f"시작시간: {str(datetime.now())}")
print("-" * 50)

def check_port(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)

        result = s.connect_ex((ip, port))
        if result == 0:
            print(f"[+] {port}번 포트가 열려있습니다")
        s.close()
    except:
        pass

try:
    for port in range(1, 1025):
        check_port(target, port)

except KeyboardInterrupt:
    print("\n[!] 사용자가 강제로 중단했습니다")
finally:
    print("-" * 50)
    print("스캔이 완료되었습니다")