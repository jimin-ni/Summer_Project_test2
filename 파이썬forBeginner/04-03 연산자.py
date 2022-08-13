##  동전 교환 프로그램  ##

# 변수 초기화
value = 0
FiveHundsWon = 0
OneHundsWon = 0
FiftiethWon = 0
TenWon = 0
num = 0

# 함수 설정
FiveHundsWon = int(input('500원짜리 개수 --> '))
OneHundsWon = int(input('100원짜리 개수 --> '))
FiftiethWon = int(input('50원짜리 개수 --> '))
TenWon = int(input('10원짜리 개수 --> '))
num = 500*FiveHundsWon + 100*OneHundsWon + 50*FiftiethWon + 10*TenWon

# 출력 결과문
print('##동전의 합계 => ', num, '원')