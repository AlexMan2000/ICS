#暴力递归
def maxCoins(nums):
    def dfs(nums, size, depth, path, used, res):
        if depth == size:
            res.append(path.copy())
            return
        for i in range(size):
            # 没用过就添加，用过就跳过
            if not used[i]:
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                used[i] = True
                path.append(nums[i])
                dfs(nums, size, depth + 1, path, used, res)
                used[i] = False
                path.pop()

    def get_coins(permutation):
        tmp = nums[:]
        sum_coins = 0
        for ele in permutation:
            index = tmp.index(ele)
            if len(tmp) == 1:
                sum_coins += tmp[index]
            elif index == 0:
                sum_coins += tmp[1]*tmp[0]*1
            elif index == len(tmp)-1:
                sum_coins += tmp[index-1]*tmp[index]*1
            elif 0 < index < len(tmp)-1:
                sum_coins += tmp[index-1]*tmp[index]*tmp[index+1]
            tmp.remove(ele)
        return sum_coins

    size = len(nums)
    if size == 0:
        return []
    nums_sorted = sorted(nums)

    used = [False] * len(nums)
    res = []
    dfs(nums_sorted, size, 0, [], used, res)
    max_coins_list = []
    for permutation in res:
        max_coins_list.append(get_coins(permutation))
    return max(max_coins_list)


print(maxCoins([3, 1, 5, 8]))
print(maxCoins([3,5,1,8]))
print(maxCoins([4, 2, 8, 3, 1, 7]))



# #不会
# def fast_maxCoins(nums):
#     #定义dp数组,dp[i]为
#     [1,3,1,5,8,1]
#     nums.append(1)
#     nums.insert(0,1)
#     length = len(nums)
#     dp = [[0,0] for i in range(length)]
#     dp[1][1] = nums[0]*nums[1]*nums[2]
#     dp[1][0] = 0
#     for i in range(2,length-1):
#         dp[i][0] = max(dp[i-1][0],dp[i-1][1])
#         dp[i][1] = max(dp[i-1][0]+nums[i-1]*nums[i]*nums[i+1],dp[i-1][1]+nums[i-2]*nums[i]*nums[i+1])
#         print(dp)
#     return dp[-2][1]
#
# print(fast_maxCoins([3,1,5,8]))
# print(fast_maxCoins([3,5,1,8]))
# print(fast_maxCoins([4,2,8,3,1,7]))
