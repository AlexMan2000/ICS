def check(lst):
    if len(lst) == 1:
        return lst[0]
    return min(lst[-1],check(lst[:-1]))
print(check([8,100,3,6]))



class ICS:
    def __init__(self,name,score):
        self.score = score
        self.name = name

    def set_score(self,new_score):
        self.score = new_score

    def get_score(self):
        return self.score

    def __str__(self):
        return "ICS is "+("supper " if self.score > 60 else '') +'fun!'


print(ICS('John',82))


class Point:
    def __init__(self,x = 0,y = 0):
        self.x = x
        self.y = y

    def __sub__(self, other):
        x = abs(self.x-other.x)
        y = abs(self.y - other.y)
        return Point(x,y)


p1 = Point(1,2)
p2 = Point(3,4)
result = p1-p2
print(result.x,result.y)