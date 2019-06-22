letter = str(input("Welcome to our shop, what do you want (C, R, U, D)?"))
sg = ["C","R","U","D"]
item = ["T-Shirt", "Sweater"]

while True:
    while letter not in sg:
        letter = str(input("Wrong! What do you want (C, R, U, D)?"))

    if letter == "R":
        print("Our items:", end=" ")
        for i in range(len(item)):
            if i == len(item)-1:
                print(item[i])
            else:
                print(item[i], end =", ")

    if letter == "C":
        new_item = str(input("Enter new item: "))
        item.append(new_item)
        print("Our items:", end=" ")
        for i in range(len(item)):
            if i == len(item)-1:
                print(item[i])
            else:
                print(item[i], end =", ")

    if letter == "U":
        pos = int(input("Update position? "))
        update_item = str(input("New item? "))
        item[pos-1] = update_item
        print("Our items:", end=" ")
        for i in range(len(item)):
            if i == len(item)-1:
                print(item[i])
            else:
                print(item[i], end =", ")

    if letter == "D":
        d = int(input("Delete position? "))
        del item[d-1]
        print("Our items:", end=" ")
        for i in range(len(item)):
            if i == len(item)-1:
                print(item[i])
            else:
                print(item[i], end =", ")

    letter = str(input("Welcome to our shop, what do you want (C, R, U, D)?"))

    if letter == "quit":
        break