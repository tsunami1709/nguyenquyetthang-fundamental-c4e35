# Viết chương trình yêu cầu người dùng nhập password, độ dài pass lớn hơn 8 ký tự, bắt buộc
# 1 kí tự số
# 1 ký tự a-z
# 1 trong 3 ký tự %, $, @

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