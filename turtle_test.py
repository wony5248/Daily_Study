import turtle
import time
t = turtle.Turtle()
t.shape("turtle")

size = 0.1
while size <= 10:
    t.shapesize(size,size)
    time.sleep(1)
    size += 1

for i in range(10):
    t.shapesize(1+i,1+i)
    time.sleep(1)

size =1
for i in range(10):
    t.shapesize(size, size)
    time.sleep(1)
    size+=1
turtle.done()