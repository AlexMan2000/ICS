# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 19:41:14 2017

@author: Mebius
"""

def permute(nums):
    # return all possible permutations of nums
    # to do
    result = []
    def helper(choosed,toChoose):
        if len(toChoose) == 0:
            result.append(choosed[:])
        for i in toChoose:
            choosed.append(i)
            toChoose.remove(i)
            helper(choosed,toChoose[:])
            choosed.pop()
            toChoose.insert(0,i)

    helper([],nums)
    return result


def main():
    num_list = [1,2,3]
    print(permute(num_list)) # Expected output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [3, 1, 2], [2, 3, 1], [3, 2, 1]]


'''
note: 
To get autograded on gradescope, you program can't print anything.

Thus, please comment out the main function call below, if you are submitting for auto grading.
'''

if __name__ == '__main__':
    main()
