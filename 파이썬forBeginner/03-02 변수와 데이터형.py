# 진수 변환

value = int(input('입력 진수 결정 : 16/10/8/2 : '))


#num은 10진수
if (value != 16 and value != 10 and value != 8 and value != 2):           # 16, 8, 10, 2 아닌 다른 수를 입력하면 아래의 문장을 프린트하도록 만든다.
    print('지정된 숫자 16, 10, 8, 2 중 하나만 골라 적으세요.')
newnum = input('값 입력 :')


if value == 16:
    num10 = int(newnum, 16)       #16진수를 10진수로 변환
elif value == 10:
    num10 = newnum                #10진수는 그대로
elif value == 8:
    num10 = int(newnum, 8)       #8진수를 10진수로 변환
elif value == 2:
    num10 = int(newnum, 2)       #2진수를 10진수로 변환



print('16진수 ===>', hex(num10))  #변환된 10진수 값을 다시 16진수로 
print('10진수 ===>', num10)       #변환된 10진수 값을 다시 10진수로 
print('8진수 ===>', oct(num10))   #변환된 10진수 값을 다시 8진수로 
print('2진수 ===>', bin(num10))   #변환된 10진수 값을 다시 2진수로 
