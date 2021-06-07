import turtle
import time
import os
import math
def textflow(text):
    for n in range(len(text)):
        print(text[n], end="")
        time.sleep(0.02)
def drawer():
    hey.color("red")
    for n in range(pointnum*j):
        x=(n/j-pointnum/2)
        if x!=0 and x!=2:
            y=x**2          #Write your function in this line
        if n>0:
            if y<-pointnum/2-2 or y>pointnum/2+4:
                continue
        if n==0:
            hey.penup()
        hey.goto(x*somenum,y*somenum)
        if n==0:
            hey.pendown()
def ptnum():
    for n in range(pointnum):
        hey.right(90)
        hey.forward(2)
        hey.backward(4)
        hey.forward(2)
        hey.left(90)
        hey.forward(400/pointnum)
    hey.right(150)
    hey.forward(10)
    hey.backward(10)
    hey.right(60)
    hey.forward(10)
    hey.backward(10)
    hey.left(30)
def putnum():
    for n in range(pointnum):
        if (n-pointnum/2)==0:
            print("")
        else:
            hey.write(int(n-pointnum/2))
        hey.penup()
        hey.backward(400/pointnum)
        hey.pendown()
text1="Hello World! "
text2="Please input the interval of an axis: "
textflow(text1)
time.sleep(2)
print("\n")
textflow(text2)
pointnum=int(input(""))
if pointnum%2==1:
    pointnum+=1
if pointnum>20:
    j=50
elif pointnum<7:
    j=100
else:

    j=70
hey=turtle.Turtle()
hey.speed(0)
hey.color("black")
somenum=400/pointnum
hey.hideturtle()
hey.penup()
hey.backward(200)
hey.pendown()
ptnum()
hey.goto(0,0)
hey.right(90)
hey.penup()
hey.backward(200)
hey.pendown()
ptnum()
hey.penup()
hey.goto(-206,-15)
hey.pendown()
hey.right(90)
putnum()
hey.penup()
hey.goto(-15, -208)
hey.left(90)
putnum()
hey.penup()
hey.goto(0,0)
hey.pendown()
drawer()
os.system("pause")
#time.sleep(10)#######
