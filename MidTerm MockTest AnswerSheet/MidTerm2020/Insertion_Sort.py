
def insertionSort(lissy):
    for i in range(1,len(lissy)):
        m = i
        while m >= 1 and lissy[m] < lissy[m-1]:
            temp = lissy[m]
            lissy[m] = lissy[m-1]
            lissy[m-1] = temp
            m -= 1
    return lissy
print(insertionSort([1,4,2,3,5]))



