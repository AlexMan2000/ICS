class Bucketsort:

    def __init__(self, inputList, bucketWidth = 10):
        self.bucketWidth = bucketWidth
        self.buckets = {}
        self.data = inputList
        self.sorted = False

    def change_bucketWidth(self, newWidth):
        """ update bucket width to the new width
        need to implement this
        """
        self.bucketWidth = newWidth


    def _distributeElementsIntoBuckets(self):
        """
        iterate through each element of data
        and put it in the corresponding bucket
        need to implement this
        """
        for i in self.data:
            if self.buckets.get(i//self.bucketWidth,0) == 0:
                self.buckets[i//self.bucketWidth] = []
            self.buckets[i//self.bucketWidth].append(i)


    def sort(self):
        """ sort data
            need to implement this part
        """

        if not self.sorted:
            # if the data has not been sorted yet, APPLY BUCKET SORT.
            # sort each bucket and combine different bucket
            self._distributeElementsIntoBuckets()
            tmp = []
            for i in sorted(self.buckets.values()):
                i.sort()
                tmp.append(i)
            result = []
            for i in tmp:
                result.extend(i)
            self.sorted = True
            self.data = result

        else:
            # if data is already sorted print the following message
            print('the data is already sorted')

'''
note: 
To get autograded on gradescope, you program can't print anything.

Thus, please comment out the main function call, if you are submitting for auto grading.
'''


# if __name__ == "__main__":
#     ## main
#     import random
#
#     random.seed(0)
#
#     listA = []
#     for i in range(100):
#         a = random.randint(0, 100)
#         listA.append(a)
#     print(listA)
#
#     BktSort = Bucketsort(listA)
#     BktSort.sort()
#     print("SORTED:", BktSort.data)
