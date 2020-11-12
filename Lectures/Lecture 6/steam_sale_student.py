


games = [(190, 10), (300, 15), (180, 10), (20, 2), (35, 5), (10, 1)]


def max_val(lst, space):
    if lst == [] or space == 0:
        return [], 0

    # if the first game in lst is too big for the available space
    elif lst[0][1] > space:
        selection, val = max_val(lst[1:], space)
        return selection, val

    # if the first game in lst is eligible for the space
    else:
        """"when lst[0] is eligible, there are two senarios: 
        1. the best solution contains lst[0]
        2. the best solution does not contain lst[0"""

        # best value with presence of lst[0]


        # best value without presence of lst[1]

        return


max_val(games, 20)

