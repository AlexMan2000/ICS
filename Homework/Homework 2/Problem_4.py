def judgeSorted(lissy):
    n = len(lissy)
    if n <= 2:
        return True
    else:
        i = 1
        j = 1
        while i < n:
            if lissy[i-1] != lissy[i]:
                j = i
                break
            i+=1
        if lissy[j] > lissy[j-1]:
            for t in range(j+1,n):
                if lissy[t-1] > lissy[t]:
                    return False
        else:
            for t in range(j+1,n):
                if lissy[t-1] < lissy[t]:
                    return False
        return True


