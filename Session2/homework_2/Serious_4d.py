n = int(input("Nhập 1 số nguyên dương: "))
for i in range(1, n+1):
    if i % 2 == 1:
        print("x ", end="")
    else:
        print("* ", end="")

