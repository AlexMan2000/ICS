#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 20:05:43 2019

@author: xg7
"""

def quicksort(seq):
    if len(seq) <= 1:
        return seq
    low, pivot, high = partition(seq)
    return quicksort(low) + [pivot] + quicksort(high)

def partition(seq):
    """complete the function"""
    pivot, seq = seq[0], seq[1:] #pick the first element as pivot
    low = []
    high = []

    # iterate through each element of the list and put it in either 'low' or 'high'
    for i in seq:
        if i >= pivot:
            low.append(i)
        else:
            high.append(i)
    return low, pivot, high


##main
listA = [9, 7, 6, 4, 2, 7, 8, 13, 1]
print("Before sorting: ", listA)
print("After sorting:", quicksort(listA))



