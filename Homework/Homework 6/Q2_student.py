import random
random.seed(0)

SIZE = 10
LOGGING = True


class PancakeStack():
    def __init__(self, stack = None):
        self.stack = stack
        self.sorted = False

    def get_size(self):
        return len(self.stack)

    # All of the pancakes are sorted after *index*
    # Returns the index of largest unsorted pancake
    def find_largest_pancake(self, index):
        largest_index = index
        #------your code here -----#
        tmp = -float('inf')
        for i in range(index+1):
            if self.stack[i] >= tmp:
                tmp = self.stack[i]
                largest_index = i
        #------end of your code----#

        if LOGGING:
            print("Insert the pan at index %d with the largest in flip as %d" \
                  %(largest_index, self.stack[largest_index]))
        return largest_index

    # Slide the pan under pancake at desired index and flip to top
    def flip(self, index):

        #------your code here -----#
        for i in range(index//2+1):
            self.stack[i],self.stack[index-i] = self.stack[index-i],self.stack[i]



    def sort_pancakes(self):

        # sort the pancakes
        if self.sorted == True:
            return

        pancakes_size = self.get_size()
        for i in reversed(range(pancakes_size)):
            flip_index = self.find_largest_pancake(i)
            self.flip(flip_index)
            if LOGGING: print("Flip Up", self.stack)
            self.flip(i)
            if LOGGING: print("Flip Down", self.stack)
        self.sorted = True

'''
note: 
To get autograded on gradescope, you program can't print anything.

Thus, please comment out the main function call below, if you are submitting for auto grading.
'''

# if __name__ == "__main__":
#     my_stack = random.sample(range(1, 20), SIZE)
#     print("Unsorted pancakes:", my_stack)
#     case_one = PancakeStack(my_stack)
#     # sort the pancakes
#     case_one.sort_pancakes()
#     print("Final order of pancakes: ", case_one.stack)
