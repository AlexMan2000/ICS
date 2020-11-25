class Tester:
    def __init__(self):
        self.idx = 0
        self.points =[1,3,5,7]

    def __iter__(self):
        self.idx = 0
        return self

    def __next__(self):
        if self.idx <= len(self.points):
            self.idx += 1
            result = self.points[self.idx]
            return result
        else:
            raise StopIteration

test = Tester()
for i in test:
    print(i)