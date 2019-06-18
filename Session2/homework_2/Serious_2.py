print("Chương trình tính giai thừa.")
n = int(input("Nhập số tự nhiên cần tính giai thừa: "))
S = 1
if n == 0:
    print(n, end="")
    print("! = ", S)
else:
    for i in range(1, n+1):
        S = S * i
    print(n, end="")
    print("! = ", S)
