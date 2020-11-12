from Retail_item import RetailItem


class CashRegister:
    def __init__(self):
        self.items = []

    def purchase_item(self, item):
        # add item to the list
        # to do
        self.items.append(item)

    def get_total(self):
        # return the total price of all the RetailItem in CashRegister
        # to do
        return sum([i.price*i.units for i in self.items])

    def get_total_items(self):
        # return the total units of all the RetailItem in CashRegister
        # to do
        return sum([j.units for j in self.items])

    def show_items(self):
        print("Description | Units in Inventory | Price")
        # display data about the RetailItem in CashRegister
        # to do
        for t in self.items:
            print('{0} | {1} | {2}'.format(t.desc,str(t.units),str(t.price)))

    def clear(self):
        # clear the CashRegister
        # to do
        self.items = []

'''
note: 
To get autograded on gradescope, you program can't print anything.

Thus, please comment out the main function call below, if you are submitting for auto grading.
'''

if __name__ == '__main__':
    register = CashRegister()
    while True:
        print("You have " + str(register.get_total_items()) +
              " items in your cart")
        print("Select which items to purchase, then press 5 to check out.")
        print("(1) Jacket ($59.95 each)")
        print("(2) Designer Jeans ($34.95 each)")
        print("(3) Shirt ($24.95 each)")
        print("(4) Clear cart")
        print("(5) Checkout")


        selection = input("> ")
        if (selection == "1"):
            print("How many jackets do you want?")
            num = int(input("> "))
            register.purchase_item(RetailItem("Jacket", num, 59.95))
        elif (selection == "2"):
            print("How many designer jeans do you want?")
            num = int(input("> "))
            register.purchase_item(RetailItem("Designer Jeans", num, 34.95))
        elif (selection == "3"):
            print("How many designer jeans do you want?")
            num = int(input("> "))
            register.purchase_item(RetailItem("Shirt", num, 24.95))
        elif (selection == "4"):
            register.clear()
        elif (selection == "5"):
            register.show_items()
            print("Your total is %.2f dollars" % register.get_total())
            break
        else:
            print("Invalid selection")
