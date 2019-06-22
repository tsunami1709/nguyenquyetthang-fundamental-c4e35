# while True:
#     print("hi")

# i = 0
# while i<10:
#     print("Hi", i)
#     i += 1

# i = 0
# while True:
#     print("Hi", i)
#     i += 1
#     if i >=10:
#         break
    
# v = 0
# while True:
#     v += 1
#     if v>10:
#         continue
#     if v>10:
#         break
#     print("hi2")

# for i in range(10):
#     if i == 3:
#         break
#     print(i)

# loop = True
# v = 0
# while loop:
#     print("hi")
#     v += 1
#     loop = v>3

# p = input("Mời bạn nhập password: ")
# while len(p) <= 8: 
#     print("Mật khẩu không đúng yêu cầu!")
#     p = input("Mời bạn nhập password: ")

# p = input("Nhập password: ")
# print(list(p)[1])

# a = "1"
# b = a
# b = "2"
# print(a)

# a = [x*x for x in range(100)]
# print(a)

# n = int(input("Nhập một số n từ bàn phím: "))
# ls=[]
# chan = 0
# tong = 0
# for i in range(n):
#     a = int(input("Nhập số nguyên thứ " + str(i+1) + ": "))
#     ls.append(a)
#     if ls[i] % 2 == 0:
#         chan += 1
#         tong += ls[i]
# print("Dãy số là:",ls)
# print("Trung bình các số chẵn là:", tong/chan)

#"a"<=s<="z
#string:...
#acsii

# #Nhập số nguyên tố n 0<=n<=1000000, phân tích n ra thừa số nguyên tố
# n = int(input("Nhập 1 số n sao cho 0 <= n <= 1000000: "))
# while n<0 and n>100000:
#     n = int(input("Nhập lại. Nhập 1 số n sao cho 0 <= n <= 1000000: "))
# a = n
# ls = []
# for i in range(2, n+1):
#     if a==1:
#         break
#     k = 0
#     for j in range (2,i+1):
#         if i % j == 0:
#             k=k+1
#     if k == 1:
#         while a % i == 0:
#             a = a/i
#             ls.append(i)
# print(ls)

#Kiểm tra password

thuong = []
so = []
dac_biet = ["%","$","@"]
for i in range (97,123):
    thuong.append(chr(i))
for i in range (48,58):
    so.append(chr(i))
p = input("Nhập password từ bàn phím:")
while True:
    dem_thuong = 0
    dem_so = 0
    dem_dac_biet = 0
    for i in range(len(p)):
        if list(p)[i] in thuong:
            dem_thuong += 1
    for i in range(len(p)):
        if list(p)[i] in so:
            dem_so += 1
    for i in range(len(p)):
        if list(p)[i] in dac_biet:
            dem_dac_biet += 1
    if dem_thuong == 0 or dem_so == 0 or dem_dac_biet == 0 or len(p)<8:
        p = input("Nhập lại password từ bàn phím:")
    else:
        break 
print("Password ok!")