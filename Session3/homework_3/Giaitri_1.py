image = []
row = int(input("Nhập số hàng: "))
col = int(input("Nhập số cột: "))

#input ma trận m hàng n cột
for i in range(row):
    image.append([])
    for j in range(col):
        image[i].append(0)
for i in range(row):
    for j in range(col):
        so = int(input("Nhập số ở hàng " + str(i+1) + " cột " + str(j+1) + ": "))
        image[i][j] = so

#input filter
fil = [[1,0,1],[0,1,0],[1,0,1]]

#tạo convolved_feature
convolved_feature = []
for i in range(row-2):
    convolved_feature.append([])
    for j in range(col-2):
        convolved_feature[i].append(0)
for i in range(row-2):
    for j in range(col-2):
        k1 = image[i][j]*fil[0][0] + image[i][j+1]*fil[0][1] + image[i][j+2]*fil[0][2]
        k2 = image[i+1][j]*fil[1][0] + image[i+1][j+1]*fil[1][1] + image[i+1][j+2]*fil[1][2]
        k3 = image[i+2][j]*fil[2][0] + image[i+2][j+1]*fil[2][1] + image[i+2][j+2]*fil[2][2]
        convolved_feature[i][j] = k1 + k2 + k3

#in convolved_feature
for i in range(row-2):
    for j in range(col-2):
        print(convolved_feature[i][j], end=" ")
        if j == col - 3:
            print()



