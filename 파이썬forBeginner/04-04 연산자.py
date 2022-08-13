# 10진수 이진수로 변환해 거북이로 표현하기 
    

import turtle

num = 0
swidth, sheight = 1000, 300
curX, curY = 0, 0

if __name__ == "__main__" :
    turtle.title('거북이로 2진수 표현하기')
    turtle.shape('turtle')
    turtle.setup(height= sheight + 30, width= swidth +30)
    turtle.screensize(swidth, sheight)
    turtle.penup()
    turtle.left(90)

    num = int(input('숫자를 입력하세요 : '))
    binary = bin(num)
    curX = swidth / 2                                   #거북이의 초기 위치를 윈도창 오른쪽 끝으로 배치
    curY = 0
    for i in range(len(binary) -2 ):
        turtle.goto(curX, curY)
        if num & 1:                 # 이해가 잘 안됌     #입력받은 수를 이진수로 변환, 하위 비트가 1 -> true 빨강 | o->False 파랑
            turtle.color('red')
            turtle.turtlesize(2)
        else:
            turtle.color('blue')
            turtle.turtlesize(1)
        turtle.stamp()
        curX -= 50
        num >>= 1                                       #숫자를 오른쪽으로 1 쉬프트시킨다.
    
turtle.done()
