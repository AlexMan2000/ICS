from item import *

# You'll need to sort the item list by the metric you're using to be greedy
def greedy(items, max_space, keyFunction):
    items_copy = sorted(items, key=keyFunction, reverse=True)
    result = []
    total_value = 0.0
    total_space = 0.0

    for i in range(len(items_copy)):
        if (total_space + items_copy[i].getSpace()) <= max_space:
            result.append(items_copy[i])
            total_space += items_copy[i].getSpace()
            total_value += items_copy[i].getValue()

    return (result, total_value)




# Tests a given greedy method (items must be sorted first)
def test_greedy(items, constraint, keyFunction):
    purchased, val = greedy(items, constraint, keyFunction)
    print('Total value of items purchased = ', val)
    for item in purchased:
        print(item)


# Testing value, weight, and density greedy approaches
def test_greedys(max_space=20):
    items = buildItems()
    print("Filling your 20GB space with the most valuable games: ")
    test_greedy(items, max_space, value)
    print("\nFilling your 20GB space with as many games as possible: ")
    test_greedy(items, max_space, spaceInverse)
    print("\nFilling your 20GB space with high value/size games: ")
    test_greedy(items, max_space, density)


test_greedys(20)
