def Bubble_Tea(lissy):
    for i in range(1,len(lissy)):
        for j in range(0,len(lissy)-1):
            if lissy[i] < lissy[j]:
                lissy[i],lissy[j] = lissy[j],lissy[i]
    return lissy


def Bubble_Tea_2(lissy):
    for i in range(0,len(lissy)):
        swap = 0
        for j in range(0,len(lissy)-1):
            if lissy[j] > lissy[j+1]:
                lissy[j],lissy[j+1] = lissy[j+1],lissy[j]
                swap += 1
        if swap == 0:
            break
    return lissy


def Bubble_Tea_Optimized(lissy):
    for i in range(0,len(lissy)):
        swap = 0
        for j in range(0,len(lissy)-1-i):
            if lissy[j] > lissy[j+1]:
                lissy[j],lissy[j+1] = lissy[j+1],lissy[j]
                swap += 1
        if swap == 0:
            break
    return lissy
print(Bubble_Tea_2([1,3,2,4,3,6,2,1,3]))

