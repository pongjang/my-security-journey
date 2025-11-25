import socket
import threading
from datetime import datetime

target = input("타겟 ip를 입력하세요")

print("-" * 50)
print(f"배너 그래빙 스캔 시작: {target}")
print("-" * 50)

def check_port(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)

        result = s.connect_ex((ip, port))

        if result == 0:
            try:
                banner = s.recv(1024).decode().strip()
                print(f"[+] {port}번 포트 (open) : {banner}")
            except:
                print(f"[+] {port}번 포트 (open) : (배너 정보 없음)")
        s.close()
    except:
        pass

threads = []

common_ports = list(range(1, 1024)) + [3306, 8080]

for port in common_ports:
    t = threading.Thread(target=check_port, args=(target, port))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
print("-" * 50)
print("스캔 완료")