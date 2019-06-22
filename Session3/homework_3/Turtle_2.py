from turtle import *

colors = ['red','blue','brown','yellow','grey']

for i in range (5):
    penup()
    forward(50)
    pendown()
    color(colors[i])
    begin_fill()
    for i in range(2):
        right(90)
        forward(100)
        right(90)
        forward(50)
    end_fill()
    
mainloop()