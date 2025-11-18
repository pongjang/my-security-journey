def print_my_goal():
    print("---함수 1 실행---")
    print("AI와 정보보안의 융합(AI 레드팀) 과정을 체계적으로 학습하는것")

def add_two_numbers(num1,num2):
    print("---함수 2 실행---")
    result = num1 + num2
    return result

print_my_goal()

a_result = add_two_numbers(10,20)
print("10+20의 결과:", a_result)
b_result = add_two_numbers(5,5)
print("5+5의 결과:",b_result)