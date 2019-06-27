#Nhập số nguyên tố n 0<=n<=1000000, phân tích n ra thừa số nguyên tố

n = int(input("Nhập 1 số n sao cho 0 <= n <= 1000000: "))
while n<0 and n>100000:
    n = int(input("Nhập lại. Nhập 1 số n sao cho 0 <= n <= 1000000: "))
a = n
ls = []
for i in range(2, n+1):
    if a==1:
        break
    k = 0
    for j in range (2,i+1):
        if i % j == 0:
            k=k+1
    if k == 1:
        while a % i == 0:
            a = a/i
            ls.append(i)
print(ls)

dic ={}
for v in ls:
    if v not in dic:
        dic[v] = 0
    dic[v] += 1

print(dic)

print(n, "=", end=" ")

s = ""
for  v in dic:
    if dic[v] == 1:
        s = s + '{}x'.format(v,dic[v])
    else:
        s = s + '{}^{}x'.format(v,dic[v])

if len(s) > 0:
    s = s[0:len(s)-1] 
print(s)
