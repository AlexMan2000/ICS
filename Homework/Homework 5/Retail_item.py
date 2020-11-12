class RetailItem:
    def __init__(self, desc, units, price):
        self.desc = desc
        # to do
        self.units = units
        self.price = price


    def get_description(self):
        # to do
        return self.desc

    def set_description(self, desc):
        # to do
        self.desc = desc

    def get_price(self):
        # to do
        return self.price

    def set_price(self, price):
        # to do
        self.price = price

    def get_units(self):
        # to do
        return self.units

    def set_units(self, units):
        # to do
        self.units = units

    def __str__(self):
        return self.desc + " | " + str(self.units) + " | $" + str(self.price)

def main():
    # create three RetailItem and append them to items list
    items = []
    items.append(RetailItem("Jacket", 12, 59.95))
    # to do
    items.append(RetailItem("Designer Jeans",40,34.95))
    items.append(RetailItem("Shirt",20,24.95))
    # the following return statement is used for autograding solely
    # it will not affect your program
    return items


'''
note: 
To get autograded on gradescope, you program can't print anything.

Thus, please comment out the main function call below, if you are submitting for auto grading.
'''

if __name__ == '__main__':
    main()

