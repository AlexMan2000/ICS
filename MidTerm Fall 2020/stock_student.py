

# note you can change the format of the function if you prefer to
# for example you can define your function as max_profit(arr, start, end)
def max_profit(arr):
    """ implement """
    total = 0
    dp_i_1 = -float('inf')
    for i in range(len(arr)):
        tmp = total
        total = max(total, dp_i_1 + arr[i])
        dp_i_1 = max(dp_i_1, tmp - arr[i])
    return total



arr = [100, 180, 260, 310, 40, 535, 695]
print(max_profit(arr))
arr =[19, 20, 14, 15, 18, 15, 17]
print(max_profit(arr)) 

