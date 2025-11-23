import socket
import threading
from datetime import datetime

target = input("타겟 ip를 입력하세요")

print("-" * 50)
print(f"고속 스캔 시작: {target}")
print(f"시작 시간: {str(datetime.now())}")
print("-" * 50)

def check_port(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)

        result = s.connect_ex((ip, port))
        if result == 0:
            print(f"[+] {port}번 포트가 열려있습니다")
        s.close()
    except:
        pass

threads = []

for port in range(1, 1025):
    t = threading.Thread(target=check_port, args=(target, port))
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()

print("-" * 50)
print("스캔종료")
print(f"종료시간: {str(datetime.now())}")