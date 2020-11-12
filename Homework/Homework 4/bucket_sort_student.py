import random
random.seed(0)

def bucket_sort(mylist):
    # initialize the buckets
    mydict = {}

    # place the values to be sorted in the buckets
    for i in mylist:
        if mydict.get(i // 10, 0) == 0:
            mydict[i // 10] = []
        mydict[i // 10].append(i)
    # sort each bucket
    tmp = []
    for i in sorted(mydict.values()):
        i.sort()
        tmp.append(i)

    result = []
    # concatenate your bucket to the result
    for i in tmp:
        result.extend(i)
    return result


'''
note: 
To get autograded on gradescope, you program can't print anything.

Thus, please comment out the main function call, if you are submitting for auto grading.
'''


# def main():
#     """ this is not exactly relevant, but the following 4 lines of
#     code can be replaced by one line:
#     list_a = [random.randint(0, 100) for i in range(1000)]
#     """
#     list_a = []
#     for i in range(1000):
#         list_a.append(random.randint(0,100))
#     print(list_a)
#
#     list_a = bucket_sort(list_a)
#     print("SORTED:", list_a)
#
# main()
