def stock_one(arr):
    n = len(arr)
    #定义dp数组
    dp = [[0,0] for i in range(n)]
    dp[-1][1] = -float('inf')
    dp[-1][0] = 0
    for i in range(n):
        dp[i][0] = max(dp[i-1][0],dp[i-1][1]+arr[i])
        dp[i][1] = max(dp[i-1][1],dp[i-1][0]-arr[i])
    return dp[-1][0]


print(stock_one([3,2,6,5,0,3]))
# print(stock_one_o([3,2,6,5,0,3],1))
# print(stock_infinity([3,2,6,5,0,3,7,9,8]))
# print(stock_infinity_cooldown([3,2,6,5,0,3]))
# print(stock_k_2([3,2,6,5,0,3,7,9,8],2))
# print(stock_k_any([3,2,6,5,0,3,7,9,8],7))