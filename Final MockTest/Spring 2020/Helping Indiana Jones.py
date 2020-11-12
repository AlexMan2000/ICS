def calculate_max_value(bag):
    return pick_items(bag)[0]

def pick_items(bag):
    all_combinations = []
    def helper(index,tmp):
        weight = 0
        for item in tmp:
            weight += bag[item]["weight"]
        if weight > 15:
            return
        all_combinations.append(tmp[:])
        for i in range(index,len(bag)):
            tmp.append(list(bag.keys())[i])
            helper(i+1,tmp)
            tmp.remove(list(bag.keys())[i])
    helper(0,[])
    max_value = -float('inf')
    best_combination = None
    for combination in all_combinations:
        value = 0
        for item in combination:
            value += bag[item]["value"]
        if value > max_value:
            best_combination = combination
            max_value = value
    return max_value,best_combination



treasure_found = {"Golden Idol":{'weight':5,"value":3},
                  "Peacock's eye":{"weight":3,"value":6},
                  "Lost Ark":{"weight":7,"value":5},
                  "Holy Grail":{"weight":2,"value":4},
                  "Crystal skull":{"weight":3,"value":3},
                  "Trunchoen":{"weight":4,"value":4}}

print(calculate_max_value(treasure_found))
print(pick_items(treasure_found))
