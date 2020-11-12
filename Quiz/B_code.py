
# Problem B
# Version A (for MorningSession)
# B1
def order(p, q, n):
    # IMPLEMENTATION
    # ---- start your code ---- #
    return p[n] < q[n]

    # ---- end of your code --- #


# B2
def first_min(order_f, l, n):
    # IMPLEMENTATION
    # ---- start your code ---- #
    i = 0
    smallest_index = 0
    while i < len(l)-1:
        print(i)
        if order_f(l[i+1],l[i],n):
            if order_f(l[i+1],l[smallest_index],n):
                smallest_index = i+1
        i += 1

    return l[smallest_index]


    # ---- end of your code --- #


# B3
def last_min(order_f, l, n):
    # IMPLEMENTATION
    # ---- start your code ---- #
    i = 0
    smallest_index = 0
    while i < len(l) - 1:
        if order_f(l[i+1],l[i],n):
            if order_f(l[i+1],l[smallest_index],n):
                smallest_index = i+1
            else:
                if l[i+1][n] == l[smallest_index][n]:
                    smallest_index = i+1
        i+=1
    return l[smallest_index]




    # ---- end of your code --- #


# testers, do not modify
t = [('Xeron', 5, 101), ('Ben', 6, 100), ('Peter', 4, 95), ('Xeron', 3, 70), ('Ben', 5, 98), ('Peter', 3, 78)]
t = [('Xeron', 5, 101), ('Ben', 6, 100), ('Peter', 7, 95), ('Xeron', 8, 70), ('Ben', 7, 98), ('Peter', 5, 78)]
print(order(('Johnny English', 35, 180), ('James Bond', 40, 185), 0))
print(order(('Johnny English', 35, 180), ('James Bond', 40, 185), 1))
print(order(('Johnny English', 35, 180), ('James Bond', 40, 185), 2))
print(first_min(order, t, 1))
print(last_min(order, t, 1))