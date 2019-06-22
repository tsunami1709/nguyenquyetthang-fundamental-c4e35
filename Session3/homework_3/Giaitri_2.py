n = int(input("Nhập số tự nhiên n: "))
m = n//2
so = 0

#tạo lập mảng có số phần tử theo yêu cầu nhưng các phần tử bằng 0
ls = []
for i in range(n):
    ls.append([])
    for j in range(n):
        ls[i].append(0)

#tạo lập mảng theo yêu cầu        
for v in range (m+1):
    j=v
    for i in range(v,n-v):
        if j==n-v-1:
            so += 1
            ls[i][j] = so
        else:
            for j in range(v,n-v):
                so += 1
                ls[i][j] = so
    if v == m:
        if n%2 == 1:
            break
        else:
            ls[m][m-1] = so
            break
    else:
        for i in range(n-v-1,v-1,-1):
            if i==v:
                continue
            else:
                if j==v:
                    so += 1
                    ls[i][j] = so
                else:
                    for j in range(n-v-2,v-1,-1):
                        so += 1
                        ls[i][j] = so

#in ra bảng theo yêu cầu
p = len(list(str(ls[m][m-1])))
for i in range(n):
    for j in range(n):
        if len(list(str(ls[i][j]))) < p:
            t = len(list(str(ls[i][j])))
            k=1
            x=" "
            while k<p-t:
                k=k+1
                x = x + " "
            print(x,end="")
            print(ls[i][j], end=" ")
        else:
            print(ls[i][j],end=" ")
        if j == n-1:
            print()
