# n = int(input("Nhập n:"))
# ls = []
# for i in range(n):
#     a = int(input("Nhập phần tử thứ " + str(i+1) + ": "))
#     ls.append(a)

# print("Dãy", ls)

# s1 = ls[0]
# k1 = 0
# for i in range(1,n):
#     if ls[i] > s1:
#         s1 = ls[i]
#         k1 = i
# print("Giá trị lớn nhất là",s1," ở vị trí",k1+1)

# s2 = ls[0]
# k2 = 0
# for i in range(1, n):
#     if ls[i] < s2:
#         s2 = ls[i]
#         k2 = i

# print("Giá trị lớn nhất là",s2," ở vị trí",k2+1)

dic = {
    'computer':'máy tính',
    'mouse':'chuột',
    'keyboard':'bàn phím'
}

t = input("Nhập vào 1 từ tiếng anh cần dịch:")
while True:
    if t in dic:
        print(t,"nghĩa là", dic[t])
        t = str(input("""Nhập từ khác. Hoặc nhập "exit" hoặc "quit" để thoát."""))
    else:
        t = str(input("""Từ này không có. Nhập từ khác. Hoặc nhập "exit" hoặc "quit" để thoát."""))
    if t in ['quit','exit']:
        break
