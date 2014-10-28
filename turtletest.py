__author__ = 'ondrej'

from turtle import *


t = Turtle()
t.speed(2000)
screen = t.getscreen()
N = 4
M = 6
P = 6
length = 50
for k in range(P):
    t.forward(4 * length)
    for j in range(M):
        t.forward(length)
        for i in range(2 * N):
            t.forward(length)
            t.left(180 - 180/N)
        t.back(length)
        t.left(360/M)
    t.back(4 * length)
    t.left(360/P)
screen.exitonclick()





