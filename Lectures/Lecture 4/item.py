class Item(object):
    # A constructor for an instance (object) of the class
    def __init__(self, n, v, s):
        self.name = n
        self.value = float(v)
        self.space = float(s)
    # Some getters for the class data members
    def getName(self):
        return self.name
    def getValue(self):
        return self.value
    def getSpace(self):
        return self.space
    # A function that returns a useful string rep of the object
    def __str__(self):
        return str("$ " + str(self.value)
                   + ",\t " + str(self.space) + ",\t" +str(self.name) )




# Returns an item's value
def value(item):
    return item.getValue()
# Returns the reciprocal of an item's weight
def spaceInverse(item):
    return 1.0 / item.getSpace()
# Returns an item's value/space ratio
def density(item):
    return item.getValue() / item.getSpace()

def buildItems():
    names = ["Civilization V" , "CS:GO", "The Elder Scrolls V" ,
                 "Torchlight II" , "Age of Empires II" , "Banished"]
    values = [190, 300, 180, 20, 35, 10]
    space = [10, 15, 10, 2, 5, 1]

    Items = []
    for i in range(len(values)):
        Items.append( Item(names[i], values[i], space[i]) )
    return Items








