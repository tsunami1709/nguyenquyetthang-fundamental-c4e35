from turtle import *
def draw_star(x,y,length):
    penup()
    setpos(x,y)
    pendown()
    left(72)
    for i in range(5):
        forward(length)
        right(144)
speed(0)
ls = ['blue','red','yellow','orange', 'green','grey']
# color('blue')
for i in range(100):
   import random
   color(random.choice(ls))
   x = random.randint(-300, 300)
   y = random.randint(-300, 300)
   length = random.randint(3, 10)
   draw_star(x, y, length)

mainloop()