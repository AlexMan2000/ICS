import random
#Bubble Sort(Optimized)(O(n^2))
def bubble_sort(lissy):
    for i in range(len(lissy)):
        swap = 0
        for j in range(len(lissy)-i-1):
            if lissy[j] > lissy[j+1]:
                lissy[j],lissy[j+1] = lissy[j+1],lissy[j]
                swap += 1
        if swap == 0 :
            return lissy
    return lissy

print('冒泡排序')
print(bubble_sort([1,4,2,3,5,6,3]))




#QuickSort(Recursion)(O(nlogn))
def quick_sort(lissy):
    def segment(lissy):
        pivot = lissy[0]
        low = []
        high = []
        for i in range(1,len(lissy)):
            if lissy[i] >= pivot:
                high.append(lissy[i])
            else:
                low.append(lissy[i])
        return low,high,pivot

    if len(lissy) == 0:
        return []

    low,high,pivot = segment(lissy)
    return quick_sort(low)+[pivot]+quick_sort(high)

print('快速排序')
print(quick_sort([1,4,2,3,5,6,3]))



#随机快速排序(O(nlogn))
def random_quick_sort(lissy_out):
    def segment(lissy):
        #将随机下标与lissy[0]交换，然后取下标的值即可
        t = random.randint(0,len(lissy)-1)
        lissy[0],lissy[t] = lissy[t],lissy[0]
        pivot = lissy[t]
        low = []
        high = []
        for i in range(0,t):
            if lissy[i] >= pivot:
                high.append(lissy[i])
            else:
                low.append(lissy[i])
        for i in range(t+1,len(lissy)):
            if lissy[i] >= pivot:
                high.append(lissy[i])
            else:
                low.append(lissy[i])
        return low,high,pivot

    if len(lissy_out) == 0:
        return []

    low,high,pivot = segment(lissy_out)
    return random_quick_sort(low)+[pivot]+random_quick_sort(high)

print('随机快速排序')
print(random_quick_sort([1, 4, 2, 3, 5, 6, 3]))




#MergeSort(Recursion)(O(nlogn))
def merge_sort(lissy):
    def merge(left,right):
        tmp = []
        while left and right:
            if left[0] <= right[0]:
                tmp.append(left.pop(0))
            else:
                tmp.append(right.pop(0))
        tmp.extend(left if left else right)
        return tmp

    if len(lissy) == 1:
        return lissy
    left = merge_sort(lissy[:len(lissy)//2])
    right = merge_sort(lissy[len(lissy)//2:])
    return merge(left,right)

print('归并排序')
print(merge_sort([1, 4, 2, 3, 5, 6, 3]))
# print(merge_sort([7, -1, -4, 100, 50, 8, -2]))




#Pancake_Sort(Iteration)(O(n^2))
def pancake_sort(lissy):
    #在lissy[0 .... index]中找到最大元素的索引
    def find_largest(index):
        largest_index = 0
        max = -float('inf')
        for i in range(index+1):
            if lissy[i] > max:
                largest_index = i
                max = lissy[i]
        return largest_index

    #翻面,将[0 ... index]的元素reverse一下
    def flip(index):
        for i in range((index+1)//2):
            lissy[i],lissy[index-i] = lissy[index-i],lissy[i]

    #主体逻辑操作
    for index in range(len(lissy)-1,-1,-1):
        large = find_largest(index)
        flip(large)
        flip(index)

    return lissy

print('烧饼排序')
print(pancake_sort([1, 4, 2, 3, 5, 6, 3]))





#计数排序(Count Sort)(时间复杂度O(n),空间复杂度O(n),仅适用于限定范围的数列的排序)
def count_sort(nums):
    place = [0] * 101
    output = []

    for n in nums:
        place[n] += 1  # 把从0 - 100的所有数的个数都数出来了。

    i = 0
    for count in place:
        for t in range(count):
            output.append(i)
        i += 1
    return output

print('计数排序')
print(count_sort([1,4,2,3,5,6,3]))






#Insertion Sort 插入排序(O(n^2))
def insertion_sort(lissy):
    for i in range(len(lissy)):
        for j in range(i):
            if lissy[j] > lissy[i]:
                lissy[j] ,lissy[i] = lissy[i],lissy[j]
    return lissy

print('插入排序')
print(insertion_sort([1,4,2,3,5,6,3]))




#(Selection_sort)选择排序(O(n^2)),找最小元素，然后交换
def selection_sort(lissy):
    for i in range(len(lissy)):
        min_index = i
        for j in range(i,len(lissy)):
            if lissy[j] < lissy[min_index]:
                min_index = j
        lissy[i],lissy[min_index] = lissy[min_index],lissy[i]
    return lissy

print('选择排序')
print(selection_sort([1,4,2,3,5,6,3]))



#(BucketSort)桶排序(O(n)),通过映射实现, 但十分消耗空间，只适用于有限定长度的数列排序
def bucket_sort(lissy):
    #定义哈希映射规则
    bucket = [0]*len(lissy)
    res = []
    for num in lissy:
        bucket[num%(len(lissy))] = num
    for i in bucket:
        if i != 0 :
            res.append(i)
    return res


print('桶排序')
print(selection_sort([1, 4, 2, 3, 5, 6, 3]))



#希尔排序,较难




















