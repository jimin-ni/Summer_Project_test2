##      마음대로 이동하는 거북이    ##
import random
import turtle

#전역변수 초기화와 선언
swidth, sheight, pSize, exitCount = 300, 300, 3, 0
r, g, b, angle, dist, curX, curY = [0]*7

#메인 코드 부분
turtle.title('마음대로 이동하는 거북이')
turtle.shape('turtle')
turtle.pensize(pSize)
turtle.setup(width = swidth + 30, height = sheight + 30)
turtle.screensize(swidth, sheight)

while True:             # 무한 반복
    r = random.random()
    g = random.random()
    b = random.random()
    turtle.pencolor((r, g, b))

    angle = random.randrange(0, 360)
    dist = random.randrange(1, 100)
    turtle.left(angle)
    turtle.forward(dist)
    curX = turtle.xcor()            #거북이 현재 x좌표
    curY = turtle.ycor()            #거북이 현재 y좌표

    if (-swidth / 2 <= curX and curX <= swidth / 2) and (-sheight / 2 <= curY and curY <= sheight / 2):
        pass
    else:
        turtle.penup()
        turtle.goto(0,0)
        turtle.pendown()

        exitCount += 1
        if exitCount >= 5 :                     #5회 이상 거북이가 밖으로 빠져나갔다면
            break                               #프로그램 종료

turtle.done()
turtle.exitonclick()                            #맘대로 창이 닫히지 않도록 설정

