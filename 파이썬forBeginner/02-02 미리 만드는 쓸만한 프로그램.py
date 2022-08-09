""" 랜덤 크기와 색깔, 각도로 거북이 도장 찍기 """
from msilib.schema import tables
import turtle
import random

# 함수 선언 
def screenRightClick(x,y) :
    global r, g, b
    r = random.random()
    g = random.random()
    b = random.random()
    turtle.pencolor((r, g, b))
    turtle.color((r, g, b))
    
    tSize = random.randrange(1, 10)
    turtle.shapesize(tSize)
    
    tAngle = random.randrange(0, 361)
    turtle.right(tAngle)

    turtle.pendown()
    turtle.stamp()
    turtle.goto(x, y)

# 변수 선언
pSize = 5                               
r, g, b = 0.0, 0.0, 0.0

#메인 코드 부분
turtle.title('거북이 도장 찍기')
turtle.shape('turtle')                          #거북이 외에도 다양한 모양 존재 : arrow, triangle, square, cicle
turtle.pensize(pSize)


turtle.onscreenclick(screenRightClick,3)        #1번이 좌클릭, 2번이 마우스 휠, 3번이 우클릭

turtle.done()               
turtle.exitonclick()                            #맘대로 창이 닫히지 않도록 설정