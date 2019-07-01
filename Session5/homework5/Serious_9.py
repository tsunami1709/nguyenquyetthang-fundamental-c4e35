def get_even_list(l):
    d = len(l)
    i = 0
    while i < d:
        if l[i] % 2 == 1:
            del l[i]
            d-=1
        else:
            i+=1
    return l
