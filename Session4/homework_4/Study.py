data = input("Enter: ")
a = data.lower()
dic = {}
for i in list(a):
    if i == " ":
        continue
    if i not in dic:
        dic[i] = 0
    dic[i] += 1

s = list(dic.items())
s.sort()
for k,v in s:
    print(k, " ", v)

