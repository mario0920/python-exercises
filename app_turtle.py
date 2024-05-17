from turtle import *
import turtle

while True:
    d = input('direction (w d a s)>')
    if d == 'qqq':
         break
    if d == 'w':
        forward(60)
    elif d == 'd':
        right(90)
    elif d == 'a':
        left(90)
    elif d == 's':
        turtle.color("red")
        bk(100)
         

print("the digith you entered")