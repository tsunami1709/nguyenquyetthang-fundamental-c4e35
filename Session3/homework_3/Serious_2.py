so_cuu = int(input("Nhập số cừu trong đàn: "))
dan_cuu = []

for i in range(so_cuu):
    a = int(input("Size của con cừu thứ " + str(i+1)+ " là: "))
    while a in dan_cuu or a<8:
        a = int(input("Size cừu phải khác nhau. Nhập lại size của con cừu thứ " + str(i+1)+ " là: "))
    dan_cuu.append(a)

print("Hello, my name is ThangThang and these are my ship sizes:")
print(dan_cuu)

print("Now my biggestbiggest sheepsheep has size", max(dan_cuu), "let's shear it")

dan_cuu[dan_cuu.index(max(dan_cuu))] = 8

print("After shearing, here ís my flock")
print(dan_cuu)

m = int(input("Nhập số tháng: "))
for i in range (1, m+1):
    print("MONTH ",i)
    for i in range(so_cuu):
        b = dan_cuu[i] + 50
        dan_cuu[i] = b
    print("One month has passed, now here is my flock")
    print(dan_cuu)
    print("Now my biggestbiggest sheepsheep has size", max(dan_cuu), "let's shear it")
    dan_cuu[dan_cuu.index(max(dan_cuu))] = 8
    print("After shearing, here ís my flock")
    print(dan_cuu)
    print()

S = 0
for i in range(so_cuu):
    S = S + dan_cuu[i]

print("My flock has sizesize in total: ", S)
print("I would get ", S, "* 2$ = ",S*2, end="")
print("$")
