# n = int(input("Nhập số phần tử (n): "))
# ls_n = []
# s1 = 0
# for i in range(n):
#     a = int(input("Nhập phần tử thứ " + str(i+1) + ": "))
#     ls_n.append(a)
#     s1 += a

# print(ls_n)
# print("Tổng dãy số vừa nhập: ",s1)
# print()

# m = int(input("Nhập số phần tử (m): "))
# ls_m = []
# s2 = 0
# for i in range(m):
#     a = int(input("Nhập phần tử thứ " + str(i+1) + ": "))
#     ls_m.append(a)
#     s2 += a

# print(ls_m)
# print("Trung bình cộng dãy vừa nhập: ", s2/m)

# def say_hi():
#     print("hi")

# say_hi()

# def add_two_number(a,b):
#     # a = int(input("nhap so thu nhat"))
#     # b = int(input("nhap so thu hai"))
#     print("tong hai so la ", a+b)
# add_two_number(4,6)

# def add_two_number(a,b):
#     return a+b

# print(add_two_number(2,3))

# def evaluate(a,b,c):
#     if c == "+":
#         return a+b
#     if c == "-":
#         return a-b
#     if c == "x":
#         return a*b
#     if c == ":":
#         return a/b
# a = int(input("Nhập số a: "))
# b = int(input("Nhập số b: "))
# c = input("Nhập phép tính (+,-,x,:): ")
# print(a, c, b, "=", evaluate(a,b,c))
def prime(a):
    if a<=0:
        return False
    if a == 1:
        return False
    for i in range(2, a):
        if a%i == 0:
            return False
    return True
# n = int(input("Nhập 1 số tự nhiên: "))
# print(prime(n))
# n = int(input("Nhập 1 số tự nhiên ở đầu: "))
# m = int(input("Nhập 1 số tự nhiên ở đầu: "))
for i in range(100, 100000):
    if prime(i):
        print(i, end=" ")