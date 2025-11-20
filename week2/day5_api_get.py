import requests

# 1. 타겟: 가짜 유저 정보가 있는 API 주소
target_url = "https://jsonplaceholder.typicode.com/users"

print(f"📡 타겟 시스템({target_url})에 접속 시도 중...")

# 2. 데이터 요청 (GET)
response = requests.get(target_url)

if response.status_code == 200:
    print("✅ 접속 성공! 데이터를 분석합니다.\n")
    
    # 3. [핵심] HTML 파싱이 아닙니다. JSON을 바로 파이썬 딕셔너리로 변환!
    # .text 대신 .json()을 씁니다.
    users = response.json()
    
    # users는 이제 '리스트(List)' 안에 '딕셔너리(Dict)'가 들어있는 형태입니다.
    
    print(f"총 {len(users)}명의 유저 정보를 탈취했습니다.")
    print("-" * 30)

    # 4. 반복문으로 정보 뽑아내기
    for user in users:
        # 딕셔너리 사용법 기억나시죠? key를 부르면 됩니다.
        name = user['name']
        email = user['email']
        company = user['company']['name'] # 딕셔너리 안에 또 딕셔너리가 있는 구조
        
        print(f"이름: {name}")
        print(f"메일: {email}")
        print(f"직장: {company}")
        print("-" * 10)
        
else:
    print("❌ 접속 실패")