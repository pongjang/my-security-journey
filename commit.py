import subprocess

def git_auto_commit():
    try:
        # 1. 변경된 파일 목록 가져오기 (git status --porcelain)
        # --porcelain 옵션은 기계가 읽기 쉽게 깔끔한 목록을 줍니다.
        status_output = subprocess.check_output(
            ["git", "status", "--porcelain"], 
            encoding="utf-8"
        )

        # 변경된 파일이 없으면 종료
        if not status_output:
            print("🙌 변경된 파일이 없습니다. 최신 상태입니다.")
            return

        print("=" * 40)
        print("📂 변경된 파일을 하나씩 커밋합니다...")
        print("=" * 40)

        # 2. 한 줄씩 읽어서 파일별로 처리하기
        for line in status_output.splitlines():
            # line 예시: "M  week2/day3_requests.py" 
            # 앞의 3글자는 상태코드(M, ?? 등)이므로 잘라내야 함
            file_path = line[3:].strip()

            # (1) 해당 파일만 무대에 올리기 (add)
            subprocess.run(["git", "add", file_path])
            
            # (2) 커밋 메시지를 "Update: 파일명"으로 자동 작성
            commit_message = f"Update: {file_path}"
            subprocess.run(["git", "commit", "-m", commit_message])
            
            print(f"✅ 커밋 완료: {commit_message}")

        # 3. 모든 커밋이 끝나면 한 번에 푸시
        print("=" * 40)
        print("🚀 GitHub로 푸시 중...")
        subprocess.run(["git", "push"])
        print("✨ 모든 작업이 완료되었습니다!")

    except subprocess.CalledProcessError as e:
        print(f"⚠️ 에러 발생: {e}")

if __name__ == "__main__":
    git_auto_commit()