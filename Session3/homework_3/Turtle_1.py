from turtle import *
colors = ['red','blue','brown','yellow','grey']
for i in range (3,8):
    color(colors[i-3])
    for j in range(i):
        forward(100)
        left(360/i)
mainloop()