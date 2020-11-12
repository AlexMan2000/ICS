#迭代器的写法
class Iter:
    def __init__(self,data):
        self.idx = 0
        self.data= data

    def __len__(self):
        return len(self.data)

    def __iter__(self): #called at the start of the loop
        self.idx = 0
        return self

    def __next__(self): #called at each incremental steps of a loop
        if self.idx < len(self):
            result = self.data[self.idx]
            self.idx+=1
            return result
        else:
            raise StopIteration

# lissy = Iter([2,1,3,4])
# for i in lissy:
#     print(i)


class A:
    def __call__(self):
        print('aa')

a = A()
a()