##  동전 교환 프로그램  ##

# 변수 초기화
value = 0
FiftiethWon = 0
OneHundsWon = 0
FiftiethWon = 0
TenWon = 0
num = 0

# 함수 설정
value = int(input('교환할 돈은 얼마인가? : '))
FiveHundsWon = value // 500
num = value % 500
OneHundsWon = num // 100
num %= 100                          # num = num % 100 과 동일의미 
FiftiethWon = num // 50
num %= 50
TenWon = num // 10
num %= 10

# 출력 결과문
print('500원짜리 ===> ', FiveHundsWon)
print('100원짜리 ===> ', OneHundsWon)
print('50원짜리 ===> ', FiftiethWon)
print('10원짜리 ===> ', TenWon)
print('바꾸지 못한 잔돈 ===> ', num)