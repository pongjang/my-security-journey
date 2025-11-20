import requests

# 1. 타겟: 데이터를 '받아주는' 창구 (URL은 같지만 용도가 다름)
target_url = "https://jsonplaceholder.typicode.com/users"

# 2. 보낼 데이터 (Payload) - 딕셔너리로 만듭니다.
# 님이 AI 해커라면 여기에 '악성 코드'나 '탈옥 명령어'를 넣겠죠?
new_user = {
    "name": "Hong Gil Dong",
    "username": "Ninja",
    "email": "hacker@korea.com",
    "company": {
        "name": "AI Security Team"
    }
}

print("📡 데이터를 생성하여 서버로 전송합니다 (POST)...")

# 3. 전송 (POST)
# json=new_user : 딕셔너리를 알아서 JSON 형식으로 포장해서 보내라!
response = requests.post(target_url, json=new_user)

# 4. 결과 확인
# 201 Created : "성공적으로 생성됨"을 뜻하는 상태 코드입니다.
if response.status_code == 201:
    print("✅ 성공! 서버가 새 유저를 등록했습니다.")
    print("📄 서버 응답(영수증):")
    print(response.json()) 
    # 보통 서버는 "그래, 내가 이거 등록했어" 하고 등록된 데이터를 다시 보여줍니다.
else:
    print(f"❌ 실패... Code: {response.status_code}")