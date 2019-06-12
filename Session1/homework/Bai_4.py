#1
from turtle import *
shape("turtle")
color("green", "yellow")
begin_fill()
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
end_fill()
mainloop()

#2
from turtle import *
shape("turtle")
color("green", "yellow")
begin_fill()
forward(100)
left(120)
forward(100)
left(120)
forward(100)
left(120)
end_fill()
mainloop()

#3
from turtle import *
shape("turtle")
color("green", "yellow")
begin_fill()
circle(50)
end_fill()
mainloop()

#4
from turtle import *
shape("turtle")
color("green")
for i in range(6):
    circle(50)
    left(60)
mainloop()

#5
from turtle import *
shape("turtle")
color("green")
speed(1000)
for i in range(100):
    circle(50)
    left(3.6)
mainloop()