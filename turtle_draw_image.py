# -*- coding: utf-8 -*-
import turtle
import numpy as np


# 데이터
img_data = np.array([[0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 1, 1, 1, 0, 0, 0, 0],
                     [1, 1, 1, 1, 1, 0, 0, 0],
                     [1, 1, 1, 1, 1, 0, 0, 0],
                     [0, 1, 1, 1, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0]])


pixelSize = 10


def putPixel(x, y, pSize, pCol):
    turtle.penup()
    turtle.goto(x*pSize, (-1)*y*pSize)
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor(pCol)
    turtle.setheading(45)
    turtle.circle(pSize/2, steps=4)
    turtle.end_fill()


for j in range(0, 8):
    for i in range(0, 8):
        if(img_data[i][j] > 0):
            putPixel(i, j, pixelSize, 'orange')

        else:
            putPixel(i, j, pixelSize, 'white')
