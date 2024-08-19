from turtle import *

speed(0)
bgcolor('black')
pensize(1)

colors = ['#AD27F5', '#e36aa5']  # Define the colors to alternate between

for i in range(16):
    color(colors[i % 2])  # Alternate between purple and pink
    for s in range(15):
        rt(90)
        circle(200 - s*6, 90)
        lt(90)
        circle(200 - s*6, 90)
        rt(180)
    circle(60, 24)

done()
