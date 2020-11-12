import matplotlib.pyplot as plt
import time
import random

def iter_search(lissy,target):
    for i in range(len(lissy)):
        if lissy[i] == target:
            return i

def binary_search(lissy,target):
    start = 0
    end = len(lissy)-1
    mid = (start+end)//2
    while start <= end:
        mid = (start+end)//2
        if lissy[mid] == target:
            return mid
        elif lissy[mid] > target:
            end = mid-1
        else:
            start = mid+1
    if lissy[start] == target:
        return start
    else:
        return -1

# def mergeSort(lissy):
#     if len(lissy) == 1:
#         return lissy
#     l1 = mergeSort(lissy[:len(lissy)//2])
#     l2 = mergeSort(lissy[len(lissy)//2:])
#     return merge(l1,l2)
#
#
# def merge(l1,l2):
#     tmp = []
#     while len(l1) > 0 and len(l2) > 0:
#         if l1[0]<l2[0]:
#             tmp.append(l1.pop(0))
#         else:
#             tmp.append(l2.pop(0))
#     while len(l2) > 0 and len(l1) == 0:
#         tmp.append(l2.pop(0))
#     while len(l1) > 0 and len(l2) == 0:
#         tmp.append(l1.pop(0))
#
#     return tmp

# print(binary_search([1,3,2,4,5],4))
# print(mergeSort([1,3,2,6,4]))

def check_func_time(func,*args):
    start_time = time.time()
    func(*args)
    end_time = time.time()
    return end_time-start_time


def plot_time_complexity(size):
    _x = [i for i in range(1,size+1)]
    _y = []
    for j in _x:
        tmp = [random.randint(0,100) for i in range(size)]
        time = check_func_time(iter_search,tmp,2)
        _y.append(time)
    print(_x)
    print(_y)
    plt.plot(_x,_y)
    plt.xlabel('size')
    plt.ylabel('time')
    plt.show()



# plot_time_complexity(100)
def tester(*args):
    print(*args)


tester([2,2,1,3,4,2],3)

