#List Span in O(1)
def distance(lissy):
    col = -1
    res = [1,]
    for i in range(1,len(lissy)):
        if lissy[i] > lissy[i-1]:
            res.append(i-col)
        else:
            col = i-1
            res.append(i-col)
    return res

print(distance([6,5,1,2,3,4,2,3,2,1]))


def all_nearest_numbers(lissy):
    stack = []
    res = []
    for i in range(len(lissy)):
        tmp_stack = stack[:]
        while tmp_stack and lissy[i] < tmp_stack[-1]:
            tmp_stack.pop()
        if not tmp_stack:
            res.append('_')
        else:
            res.append(tmp_stack.pop())

        stack.append(lissy[i])
    return res





print(all_nearest_numbers([4,2,10,8,7,20,4,15,8,14]))









