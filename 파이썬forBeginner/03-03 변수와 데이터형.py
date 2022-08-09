# 입력받은 데이터가 2, 8, 10, 16진수 중 어느것인지 확인하기.

num = input('글자 입력 :')

if (num == '0' or num == '1'):              #꼭 따옴표 안에 넣기!
    print('2진수 또는 8진수 또는 10진수 또는 16진수이다.')

elif (num == '2' or num == '3' or num == '4' or num == '5' or num == '6' or num == '7') :
    print('8진수 또는 10진수 또는 16진수이다.')

elif (num == '8' or num == '9'):
    print('10진수 또는 16진수이다.')

elif (num == 'a' or num == 'b' or num == 'c' or num == 'd' or num == 'e' or num == 'f'):
    print('16진수이다.')

else:
    print('16진수, 10진수, 8진수, 2진수도 아니다.')