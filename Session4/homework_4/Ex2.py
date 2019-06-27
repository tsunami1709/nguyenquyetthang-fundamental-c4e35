price = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3

}

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

for i in price.keys():
    if i in stock.keys():
        print(i)
        print("price: ", price[i])
        print("stock: ", stock[i])
        print()

total = {}
for i in price.keys():
    if i in stock.keys():
        total[i] = price[i]*stock[i]
        print(i, ": ", total[i])

print()
print(total)