from random import shuffle
import random

ls = ["meticulous", "champion", "hexagon"]
x = random.choice(ls)
y = list(x)
shuffle(y)

for i in range(len(y)):
    print(y[i], end=" ")
print()
a = str(input("Your answer: "))
if a == x:
    print("Hura")
else:
    print(":(")