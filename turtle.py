from turtle import *
import colorsys as cs
bgcolor('black')
tracer(100)
pensize(4)
h = 0

for i in range(550):
    c = cs.hsv_to_rgb(h,1,1)
    h += 0.008
    color(c)
    up()
    fd(i/2)
    goto(0,0)
    down()
    rt(60)
    fillcolor('black')
    begin_fill()
    circle(-i, 60)
    end_fill()
    rt(144)
    for j in ranfe(3):
        circle(j*10, 90)
        rt(105)
done()