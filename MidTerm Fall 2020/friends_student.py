# -*- coding: utf-8 -*-


mem = {0:1, 1:1}

def num_ways(n):
    """
    Find out the total number of ways
    in which 'n' friends can remain single or can be paired up.
    Hint: consider 1st person, he/she can be single or paired. 

    if you want to try big values for n, you may want to use a memory (mem) to 
    the result of redundant calculations to speed up the code. 
    """
    #------------ your code below ----------#
    if n in mem:
        return mem[n]
    if n == 0:
        return 1
    if n == 1 or n == 2:
        return n
    # #要么单着，此时方法数就是n-1个人组队的情况，要么组队，就是从n-1个人里面挑出一个单着的人，这个人单着的情况有num_ways(n-2)种。
    res = num_ways(n-1)+(n-1)*num_ways(n-2)
    mem[n] = res
    return res
    #------------ end of your code ----------#

"""
Task 2:
The complexity of the above function is: ___O(2^N)_____

"""

if __name__ == '__main__':
    print(num_ways(3))
    print(num_ways(10))
