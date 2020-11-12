import random
random.seed(0)

# Global variable that controls max size of the lists
LIMIT = 10

# Optimized bubble sort function
def bubble_sort(my_list):
# filling the bubble sort logics below
    return my_list


# Merge sort definition
def merge_sort(m):

    if len(m) <= 1:
        return m

    middle = len(m) // 2
    left = m[:middle]
    right = m[middle:]

    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)


# Merge function definition
def merge(left, right):
    result = []
#   comment out the line below and code the merge logic
    result = left + right

    return result

def main():
    randomized_lists_merge = []
    randomized_lists_bubble = []

    print("Generating randomized lists for sorting...")
    LIMIT = 10
    randomized_lists_merge = [random.randint(0, i + 1) for i in range(LIMIT)]
    print("The randomly generated list is: ", randomized_lists_merge)
    #randomized_lists_bubble = deepcopy(randomized_lists_merge)
    randomized_lists_bubble = randomized_lists_merge[:]

    print("Sorting")
#    merge_sorted_list = []
    bubble_sorted_list = bubble_sort(randomized_lists_bubble)
    print("bubble sort: ", bubble_sorted_list)

    merge_sorted_list = merge_sort(randomized_lists_merge)
    print("merge sort: ", merge_sorted_list)


main()
