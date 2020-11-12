
def quick_sort(lists):
    i = 0
    j = len(lists)-1

    def qk_sort(lists,i,j):
        if i >= j:
            return list
        pivot = lists[i]
        low = i
        high = j
        while i < j:
            while i < j and lists[j] >= pivot:
                j -= 1
            lists[i]=lists[j]
            while i < j and lists[i] <=pivot:
                i += 1
            lists[j]=lists[i]
        lists[j] = pivot
        qk_sort(lists,low,j-1)
        qk_sort(lists,j+1,high)
        return lists

    return qk_sort(lists, i, j)



##main
listA = [9, 7, 6, 4, 2, 7, 8, 13, 1]
print("Before sorting: ", listA)
print("After sorting:", quick_sort(listA))
