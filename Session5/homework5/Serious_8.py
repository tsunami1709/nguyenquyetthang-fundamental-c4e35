def remove_dollar_sign(s):
    ls = list(s)
    l = len(ls)
    i = 0
    while i < l:
        if ls[i] == "$":
            del ls[i]
            l -= 1
        i+=1
    x = ""
    for i in range(len(ls)):
        x += ls[i]
    return x

string_with_no_dollars = remove_dollar_sign("$80% percent of $life is to show $up")
if string_with_no_dollars == "80% percent of life is to show up":
   print("Your function is correct")
else:
   print("Oops, there's a bug")