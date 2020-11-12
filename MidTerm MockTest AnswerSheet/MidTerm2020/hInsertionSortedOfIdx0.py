def hInsertionSortOfIdx0(lst,h):
    for i in range(h,len(lst),h):
        m = i
        while m >= 1 and lst[m] < lst[m-h]:
            temp = lst[m]
            lst[m] = lst[m-h]
            lst[m-h] = temp
            m -= h
    return lst

print(hInsertionSortOfIdx0([9,2,0,8,5,6,1,7,3,0],4))



