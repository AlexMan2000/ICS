from Point import Point
import matplotlib.pyplot as plt
import copy


class Polygon:
    """
    A polygon class with a list of points
    """

    def __init__(self):
        self.points = []
        self.idx = 0

    def add_point(self, x, y):
        self.points.append(Point(x, y))

    def get_point(self, index):
        # check that the index is valid
        if 0 < index < len(self.points):
            return self.points[index - 1]
        else:
            return

    def plot(self):
        x = []
        y = []
        for i in range(len(self.points) - 1):
            x.append(self.points[i].x)
            x.append(self.points[i + 1].x)
            y.append(self.points[i].y)
            y.append(self.points[i + 1].y)
        x.append(self.points[0].x)
        y.append(self.points[0].y)
        plt.plot(x, y)
        plt.show()
        return

    def insert_point_at(self, x, y, index):
        if index == -1:
            self.points.insert(0,Point(x,y))
        elif index >= len(self.points):
            self.points.append(Point(x,y))
        else:
            self.points.insert(index,Point(x,y))

    def __iter__(self):
        self.idx = 0
        return self

    def __next__(self):
        if self.idx <= len(self.points)-1:
            result = self.points[self.idx]
            self.idx += 1
            return result
        else:
            raise StopIteration



class Triangle(Polygon):
    """
    A triangle class
    """

    def __init__(self):
        super().__init__()

    def remove_point(self, index):
        if 0 < index < len(self.points):
            del self.points[index]

    def add_point(self, x, y):
        if len(self.points) < 3:
            self.points.append(Point(x, y))
        else:
            print('No more points. It is a triangle')




class Rectangle(Polygon):
    """
    A rectangle class with a point as a left lower corner
    """
    def __init__(self,width,height,point):
        super().__init__()
        self.corner = point
        self.width = width
        self.height = height
        self.points.append(self.corner)
        self.points.append(Point(0, self.height))
        self.points.append(Point(self.width, self.height))
        self.points.append(Point(self.width, 0))





p1 = Polygon()
p1.add_point(0, 0)
p1.add_point(0, 3)
p1.add_point(4, 5)
p1.add_point(4, 0)

p1.plot()

for e in p1:
    print(e)

## test deep copy
p2 = copy.copy(p1)
# p1.add_point(4, 3)
p1.plot()

## test inheritence

triang_1 = Triangle()
triang_1.add_point(0, 0)
triang_1.add_point(0, 3)
triang_1.add_point(4, 0)
triang_1.plot()

for e in triang_1:
    print(e)

rect = Rectangle(5, 5, Point(0, 0))
rect.plot()

for e in rect:
    print(e)

