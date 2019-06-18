from turtle import *

for i in range(3, 7):

    k = 180*(i-2)/i 
    doi_k = 180 - k

    if i % 2 == 0:
        color("red")
    else:
        color("blue")
    
    for j in range(1, i+1):
        forward(100)
        left(doi_k)

mainloop()