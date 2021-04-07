#Author: Kean Jaycox
#Sierpinski Triangle
#2-16-2021
#version 002 - larger triangle for more definition

#This program draws an equilateral triangle, moves to a point, then proceeds
#to randomly pick one of the three corners, moves half way towards that corner,
#draws a dot, and repeats this random-move-draw process 10,000 times. A Sierpinski Triangle
#eventually emerges. With 10000 dots it takes aprox 15 minutes to finish.

import math
import random
import turtle
import time

#track how long it takes to run prog
start_time = time.time()

artist = turtle.Turtle()
artist.color('red')
artist.hideturtle()

#draw equilateral triangle
artist.penup()                      
artist.setpos(400, -350)
artist.pendown()
artist.setpos(-400, -350)
artist.setpos(0, math.sqrt(480000) - 350)
artist.setpos(400, -350)
artist.penup()

#move to a point (this is half the height and middle)
artist.setpos(0, ((math.sqrt(480000) - 350)/2))
artist.dot(4)
#draw as fast as possible
artist.speed(0)

#begin drawing dots
#number of dots
val = 10000
while(val > 0):
    #random 1,2,3 to decide which corner of triangle
    r = random.randint(1,3)
    #lower left of tri
    if r == 1:           
        #get current x & y pos           
        x = artist.xcor()
        y = artist.ycor()
        #get midpoint between cur and chosen tri corner
        midX = (-400 + x)/2
        midY = (-350 + y)/2
        #move to midpoint & dot
        artist.setpos(midX, midY)
        artist.dot(4)
    #lower right of tri
    elif r == 2:
        x = artist.xcor()
        y = artist.ycor()
        midX = (x + 400)/2
        midY = (-350 + y)/2
        artist.setpos(midX, midY)
        artist.dot(4)
    #top of tri
    elif r == 3:
        x = artist.xcor()
        y = artist.ycor()
        midX = x/2
        midY = (y + math.sqrt(480000) - 350)/2
        artist.setpos(midX, midY)
        artist.dot(4)
    #increment
    val -= 1
#output run time for drawing
print("Program took %.2f minutes to run"% ((time.time() - start_time)/60))
turtle.done()