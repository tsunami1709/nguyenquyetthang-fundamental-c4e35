# Lãi suất ngân hàng acb đang là 6.5% một năm. Hnay anh sẽ đi gửi 21 triệu. Viết chương trình để tính:
# - Sau 9 năm thì a có bao nhiêu tiền trong tài khoản?
# - Muốn mua một căn nhà giá 1.2 tỷ thì a cần gửi ngân hàng ít nhất là bao nhiêu năm?

a = 21000000
for i in range (1,10):
    a = a*106.5/100
print("Sau 9 năm thì anh có:", a)

i = 0
a = 21000000
while a < 1200000000:
    i=i+1
    a=a*106.5/100
print("Muốn mua một căn nhà giá 1.2 tỷ thì anh cần gửi ngân hàng ít nhất",i, "năm.")

