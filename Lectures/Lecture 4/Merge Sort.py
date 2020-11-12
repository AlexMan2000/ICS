def mergeSort(lissy):
    if len(lissy) == 1:
        return lissy
    l1 = mergeSort(lissy[:len(lissy)//2])
    l2 = mergeSort(lissy[len(lissy)//2:])
    return merge(l1,l2)


def merge(l1,l2):
    tmp = []
    while len(l1) > 0 and len(l2) > 0:
        if l1[0]<l2[0]:
            tmp.append(l1.pop(0))
        else:
            tmp.append(l2.pop(0))
    while len(l2) > 0 and len(l1) == 0:
        tmp.append(l2.pop(0))
    while len(l1) > 0 and len(l2) == 0:
        tmp.append(l1.pop(0))

    return tmp

tmp = mergeSort([40,20,5,4,3,2,1])
tmp.reverse()
print(tmp)
