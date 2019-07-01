def is_inside(ls1,ls2):
    if ls2[0]<ls1[0]<ls2[0]+ls2[2] and ls2[1]<ls1[1]<ls2[1]+ls2[3]:
        return True
    else:
        return False
 
print(is_inside([100, 120], [140, 60, 100, 200]))
print(is_inside([200, 120], [140, 60, 100, 200]))

