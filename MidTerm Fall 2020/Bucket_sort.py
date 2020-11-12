class Bucketsort:

    def __init__(self, bucketWidth = 10):
        self.bucketWidth = bucketWidth
        self.buckets = {}
        self.data = []
        self.sorted = False

    def change_bucketWidth(self, newWidth):
        """ update bucket width to the new width
        need to implement this
        """
        res = []
        for k,v in self.buckets.items():
            res.extend(v)
        self.bucketWidth = newWidth
        self.data = res
        self._distributeElementsIntoBuckets()


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


    def insert_ele(self,element):
        if element//self.bucketWidth not in self.buckets:
            self.buckets[element//self.bucketWidth] = []
        i = 0
        while i < len(self.buckets[element//self.bucketWidth]):
            if self.buckets[element//self.bucketWidth][i] > element:
                break
            i+=1
        self.buckets[element//self.bucketWidth].insert(i,element)


    def _merge_bucket(self):
        print(self.buckets)
        res = []
        for k,v in self.buckets.items():
            res.extend(v)
        self.data = res


    def response(self):
        self._merge_bucket()
        return self.data



if __name__ == "__main__":
    ## main
    import random

    random.seed(0)

    listA = []
    for i in range(100):
        a = random.randint(0, 100)
        listA.append(a)
    print(listA)

    BktSort = Bucketsort(10)
    BktSort.insert_ele(5)
    BktSort.insert_ele(10)
    BktSort.insert_ele(12)
    BktSort.insert_ele(19)
    BktSort.insert_ele(6)
    BktSort.insert_ele(7)
    print(BktSort.response())
