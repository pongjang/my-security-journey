import subprocess
import sys

#1. 커밋 메세지 입력하기
message = input("커밋 메시지를 입력하세요")

# 'subprocess.run'은 명령어와 결과를 완벽리 제어
def run_command(command):
    # 'command'를 실행하고, '결과(result)'를 반환받습니다.
    # capture_output=True: 터미널의 모든 출력을 'result' 변수에 담습니다.
    # text=True: 결과를 사람이 읽을 수 있는 '텍스트'로 받습니다.
    result = subprocess.run(command, capture_output=True, text=True)

    #핵심 오류처리
    #result.returncode'가 0이 아니라면(즉 오류가 나면)
    if result.returncode != 0:
        print(f"\n 오류발생! (명령어: {' '.join(command)})")
        print("---GIT 오류 메시지---")
        print(result.stderr)#git의 진짜 오류메시지 출력
        print("------------")
        print("작업중단")
        sys.exit(1) #오류로 인해 작업중지

    print(f"성공:{' '.join(command)}")
    print(result.stdout)

#-----자동화 순서------
#2.git add . 실행
run_command(["git", "add", "."])
#3. git commit 실행
run_command(["git", "commit", "-m", message])
#4. git push 실행
run_command(["git", "push"])

print("\n 자동 커밋 푸시 완료")