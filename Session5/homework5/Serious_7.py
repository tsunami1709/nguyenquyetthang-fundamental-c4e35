def remove_dollar_sign(s):
    ls = list(s)
    l = len(ls)
    i = 0
    while i < l:
        if ls[i] == "$":
            del ls[i]
            l -= 1
        else:
            i+=1
    x = ""
    for i in range(len(ls)):
        x += ls[i]
    return x

# dùng hàm có sẵn
# def remove_dollar_sign(s):
#     return s.replace("$","")

a = input("Enter:")
print(remove_dollar_sign(a))
