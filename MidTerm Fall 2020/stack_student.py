# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 15:55:36 2017

@author: Mebius
"""

class Stack:

    def __init__(self):
        # top of stack is the last item of the list
        self.items = []

    def is_empty(self):

        """is_empty should return True if the stack has no items"""
        #------your code here-------#
        return len(self.items) == 0

    def push(self, num):
        """push should add an "item" onto the top of the stack
           same as append in list,
        """
        #------your code here-------#
        self.items.append(num)

    def push_list(self, li):
        for x in li: self.push(x)

    def pop(self):
        """pop should delete the item on the top of the stack
        AND return it.  if the stack is empty, return none. 
        """
        #------your code here-------#
        return self.items.pop()

    def peek(self):
        """peek should return the item on the top of the stack
        # it should not change the stack content """
        #------your code here-------#
        if self.is_empty():
            return None
        return self.items[-1]

    def size(self):
        """size should return total number of items in the stack """
        #------your code here-------#
        return len(self.items)

    def __str__(self):
        st = '|'
        for x in self.items:
            st += ' %s |' % str(x)
        return st

## DO NOT EDIT THE MAIN CODE
if __name__ == "__main__":
    s = Stack()
    import random
    random.seed(0)
    li = [random.randint(0, 10) for i in range(10)]
    for x in li:
        s.push(x)
    print(s)

