class ICSList:
    def __init__(self,data=[]):
        self.data = data
        self.length = len(self.data)

    @property
    def len(self):
        return self.length


    def addItem(self,idx,x):
        self.data.insert(idx,x)
        self.length += 1


    def deleteItem(self,x):
        for i in range(self.length-1,-1,-1):
            if x[i] == x:
                self.data.remove(self.data[i])
                self.length -= 1

    def _getIncrements(self):
        res = []
        h = 1
        while h <= self.length:
            res.append(h)
            h = 3*h +1
        return res[::-1]

    def _hInsertionSortByIdx(self,lst,idx,h):
        for i in range(idx + h, len(lst), h):
            m = i
            while m >= idx + h and lst[m] < lst[m - h]:
                temp = lst[m]
                lst[m] = lst[m - h]
                lst[m - h] = temp
                m -= h
        return lst

    def shellSort(self):
        h_list = self._getIncrements()
        for item in h_list:
            for i in range(self.length-item+1):
                self._hInsertionSortByIdx(self.data,i,item)
    




