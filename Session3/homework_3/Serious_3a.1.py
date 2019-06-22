from random import shuffle
x = "champion"
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