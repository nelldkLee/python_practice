# 키보드로 정수 수치를 입력 받아 짝수인지 홀수 인지 판별하는 코드를 작성하세요.
data = input("수를 입력하세요: ")
if(not data.isdigit()):
    print("정수가 아닙니다.")
    exit(0)
data = int(data)

if(data % 2 == 0):
    print("짝수")
else:
    print("홀수")