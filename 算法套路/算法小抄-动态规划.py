#动态规划
import math
#零钱兑换问题(自顶向下动态规划解法)
def pick_bills(coins,amount):
    #dp[i] 定义为 当兑换金额为 i 时，需要的最小硬币数, 由于兑换金额不会超过amount,所以初始化为amount + 1 就相当于取正无穷
    dp = [amount+1]*(amount+1)
    #dp[0]不需要硬币
    dp[0] = 0
    #遍历兑换金额数的所有状态
    for i in range(len(dp)):
        #遍历金额的所有状态
        for coin in coins:
            if i - coin < 0:
                continue
            dp[i] = min(dp[i],dp[i-coin] + 1)
    return dp[amount] if dp[amount] != amount+1 else -1


#零钱兑换(自底向上递归解法,无记忆化)
def pick_bills_rec(coins,amount):
    #递归遍历兑换金额的所有状态
    def dp(n):
        if n == 0:
            return 0
        if n < 0:
            return -1
        res = math.inf
        #循环遍历所有金额的状态
        for coin in coins:
            subsolution = dp(n-coin)
            if subsolution == -1:
                continue
            res = min(res,subsolution+1)
        return res if res != math.inf else -1
    return dp(amount)


#零钱兑换(递归解法，有记忆化)
def pick_bills_recm(coins,amount):
    def dp(n,memo={}):
        if n in memo:
            return memo[n]
        if n == 0:
            return 0
        if n < 0 :
            return -1
        res = math.inf
        for coin in coins:
            subsolution = dp(n-coin)
            if subsolution < 0:
                continue
            res = min(res,1+subsolution)
        memo[n] = res if res != math.inf else -1
        return memo[n]
    return dp(amount)

# print(pick_bills([9,6,5,1],11))
# print(pick_bills_rec([9,6,5,1],11))
# print(pick_bills_recm([9,6,5,1],11))



#股票买卖(动态规划)
#本质就是穷举框架
# for 状态1 in 状态1的所有取值：
#     for 状态2 in 状态2的所有取值：
#         for ...
#             dp[状态1][状态2][...] = 择优(选择1，选择2...)


#股票买卖问题(最大交易次数为1）
def stock_one(prices,times):
    dp = [[0,0] for i in range(len(prices))]
    #还没开始的时候就持有股票，是不可能的，初始化为负无穷
    dp[-1][1] = -math.inf
    #还没开始的时候没有股票，最大利润为0
    dp[-1][0] = 0
    for i in range(len(prices)):
        #股票持有状态只有两种，所以可以简化
        dp[i][0] = max(dp[i-1][0],dp[i-1][1]+prices[i])
        dp[i][1] = max(dp[i-1][1],dp[i-1][0]-prices[i]) #可以化简为max(dp[i-1][1],-prices[i])
    return dp[-1][0]

#股票买卖问题（最大交易次数为1，缩减空间复杂度)
def stock_one_o(prices,times):
    dp_i_0 = 0
    dp_i_1 = -math.inf
    for i in range(len(prices)):
        dp_i_0 = max(dp_i_0,dp_i_1+prices[i])
        dp_i_1 = max(dp_i_1,-prices[i])
    return dp_i_0


#股票买卖问题（最大交易次数不限，缩减空间复杂度)
def stock_infinity(prices):
    dp_i_0 = 0
    dp_i_1 = -math.inf
    for i in range(len(prices)):
        tmp = dp_i_0
        dp_i_0 = max(dp_i_0,dp_i_1+prices[i])
        dp_i_1 = max(dp_i_1,tmp-prices[i])
    return dp_i_0


#股票买卖问题，(不限交易次数,有一天冷却时间)
def stock_infinity_cooldown_dp(prices):
    dp = [[0,0] for i in range(len(prices)+1)]
    dp[0][0] = 0
    dp[0][1] = -float('inf')
    dp[1][0] = 0
    dp[1][1] = -prices[0]
    for i in range(2,len(prices)+1):
        dp[i][0] = max(dp[i-1][0],dp[i-1][1]+prices[i-1])
        dp[i][1] = max(dp[i-1][1],dp[i-2][0]-prices[i-1])
    return dp[-1][0]


def stock_infinity_cooldown(prices):
    dp_i_0 = 0
    dp_i_1 = -math.inf
    dp_pre = 0 #dp[-2][0] = 0
    for i in range(len(prices)):
        tmp = dp_i_0
        dp_i_0 = max(dp_i_0,dp_i_1+prices[i])
        dp_i_1 = max(dp_i_1,dp_pre-prices[i])
        dp_pre = tmp
    return dp_i_0


#股票买卖问题，k为任意正整数,也就是限制了最大交易次数(不缩减空间复杂度)
#dp[i][k][0]定义为第i天不持有股票且最多进行了k此交易，因为K的影响不能消除，所以要对k进行穷举
#先做k = 2的情况
def stock_k_2(prices,k_max):
    dp = [[[0,0] for i in range(k_max+1)] for j in range(len(prices))]
    dp[-1][1][0] = 0
    dp[-1][2][0] = 0
    dp[-1][1][1] = -math.inf
    dp[-1][2][1] = -math.inf
    for i in range(len(prices)):
        for k in range(1,k_max+1):
            dp[i][k][0] = max(dp[i-1][k][0],dp[i-1][k][1]+prices[i])
            dp[i][k][1] = max(dp[i-1][k][1],dp[i-1][k-1][0] - prices[i])
    return dp[-1][k_max][0]

#k取任意值的情况(剪枝）
def stock_k_any(prices,k_max):
    #如果有n天，那么最多会有n//2次交易，如果k_max大于这个值，就相当于没有限制
    if k_max > len(prices)//2:
        return stock_infinity(prices)
    dp = [[[0, 0] for i in range(k_max + 1)] for j in range(len(prices))]
    for i in range(1,k_max+1):
        dp[-1][i][0] = 0
    for j in range(1,k_max+1):
        dp[-1][j][1] = -math.inf
    for i in range(len(prices)):
        for k in range(1, k_max + 1):
            dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i])
            dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 1][k - 1][0] - prices[i])
    return dp[-1][k_max][0]

print('股票买卖')
print(stock_one([3,2,6,5,0,3],1)) #7
print(stock_one_o([3,2,6,5,0,3],1)) #4
print(stock_infinity([3,2,6,5,0,3,7,9,8])) #13
print(stock_infinity_cooldown_dp([3,2,6,5,0,3])) #0
print(stock_infinity_cooldown([3,2,6,5,0,3])) #7
print(stock_k_2([3,2,6,5,0,3,7,9,8],2)) #13
print(stock_k_any([3,2,6,5,0,3,7,9,8],7)) #13

#打家劫舍问题（自顶向下递归动态规划）
def robbery_rec(money):
    memo = {}
    def helper(money,start):
        if start in memo:
            return memo[start]
        if start >= len(money):
            return 0
        res = max(helper(money,start+1),money[start]+helper(money,start+2))
        memo[start] = res
        return memo[start]
    return helper(money,0)



#打家劫舍问题（自底向上动态规划)
def robbery(money):
    #从第i间房子开始抢劫，能抢到的最多的钱为dp[i]
    #base case,dp[n+1],dp[n+2]均为零
    dp = [0]*(len(money)+2)
    #从尾部开始遍历
    for i in range(len(money)-1,-1,-1):
        dp[i] = max(money[i]+dp[i+2],dp[i+1])
    return dp[0]


#打家劫舍问题（优化空间复杂度)
def robbery_optimized(money):
    dp_i_1,dp_i_2 = 0, 0
    dp_i = 0
    for i in range(len(money)-1,-1,-1):
        dp_i = max(dp_i_1,money[i]+dp_i_2)
        dp_i_2 = dp_i_1
        dp_i_1 = dp_i
    return dp_i


#打家劫舍问题（环形链表）
#转化成固定区间上的最大打劫金额即可

print('打家劫舍')
print(robbery_rec([1,2,3,5]))
print(robbery([1,2,3,5]))
print(robbery_optimized([1,2,3,5]))


#最长公共子序列
def lcs(str1,str2):
    #这里用顶向下的递归来完成,从字符串的最后一位开始运算
    l1 = len(str1)-1
    l2 = len(str2)-1
    def helper(l1,l2):
        if l1 == -1 or l2 == -1:
            return 0
        if str1[l1] == str2[l2]:
            return helper(l1-1,l2-1)+1
        return max(helper(l1-1,l2),helper(l1,l2-1))
    return helper(l1,l2)

print('最长公共子序列')
print(lcs('abcde','ace'))


#最长公共子序列（dp数组完成)
def lcs_dp(str1,str2):
    #定义dp数组, dp[i][j]表示对于str[0...i-1],str2[0....j-1]来的最大公共子串
    l1 = len(str1)
    l2 = len(str2)
    dp = [[0]*(l2) for i in range(l1)]
    for i in range(l1):
        for j in range(l2):
            if str1[i] == str2[j]:
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    return dp[-1][-1]

print(lcs_dp('abcde','ace'))


#0-1背包问题
#weight是物品各自的重量列表，val是物品各自的价值,W是背包的最大重量
def bag(weight,val,W):
    #定义dp数组,dp[i][W]表示前面i个物品中，在背包容量为W(W>=1)的情况下的最大价值是多少
    length = len(weight)
    #初始化数组
    dp = [[0]*(W+1) for i in range(length+1)]
    #开始遍历
    #对i的i个状态遍历
    for i in range(1,length+1):
        #对W的W个状态进行遍历
        for W in range(1,W+1):
            #背包装不下,只能不装
            if W-weight[i-1] < 0:
                dp[i][W] = dp[i-1][W]
            else:
                dp[i][W] = max(dp[i-1][W],dp[i-1][W-weight[i-1]]+val[i-1])

    return dp[-1][W]
print('背包问题')
print(bag([2,1,3],[4,2,3],4))

#完全背包问题

#Steam_stale
def steam_stale(game_size,value,W):
    #定义dp数组
    #dp[i][W]表示，前[1.....i]个游戏，最大背包容量为W时的最大价值
    dp = [[0]*(W+1) for i in range(len(game_size)+1)]
    for i in range(1,len(game_size)+1):
        for W in range(W+1):
            if W-game_size[i-1] < 0:
                dp[i][W] = dp[i-1][W]
            else:
                dp[i][W] = max(dp[i-1][W],dp[i-1][W-game_size[i-1]]+value[i-1])
    return dp[-1][W]


print(steam_stale([10,15,10,2,5,1],[190,300,180,20,35,10],20))


#最大子序和（动态规划进阶)
def maximum_sum(lissy):
    #定义dp,dp[i]的含义为以lissy[i]结尾的最大子序和
    dp = [0]*len(lissy)
    for i in range(len(lissy)):
        dp[i] = max(dp[i-1]+lissy[i],lissy[i])
    return max(dp)

print('最大子序和')
print(maximum_sum([-2,1,-3,4,-1,2,1,-5,4]))


#编辑距离（递归, 无记忆化)
def manage_dis_rec(s1,s2):
    #自顶向下递归,dp(i,j)表示s1[0....i],s2[...j]的最小编辑距离
    def dp(i,j):
        #base case
        if i == -1: return j+1 #s2这时候停留在索引j处，需要往s1中插入s2中
        #剩下的所有字符
        if j == -1: return i+1 #同上
        if s1[i] == s2[j]:
            return dp(i-1,j-1)
        else:
            return min(
                dp(i,j-1)+1,   #插入
                dp(i-1,j)+1,   #删除
                dp(i-1,j-1)+1  #替换
            )
    return dp(len(s1)-1,len(s2)-1)

#编辑距离（递归，有记忆化)
def manage_dis_rec_m(s1,s2):
    def dp(i,j,memo = {}):
        if (i,j) in memo:
            return memo[(i,j)]
        if i == -1: return j+1
        if j == -1: return i+1
        if s1[i] == s2[j]:
            return dp(i-1,j-1)
        else:
            result = min(dp(i-1,j)+1,dp(i,j-1)+1,dp(i-1,j-1)+1)
            memo[(i,j)] = result
            return result

    return dp(len(s1)-1,len(s2)-1)


#编辑距离（动态规划）
def manage_dis_dp(s1,s2):
    #创建dp数组,dp[i][j]代表s1[1....i],s2[1...j]中的最短编辑距离
    l1 = len(s1)
    l2 = len(s2)
    dp = [[0]*(l2+1)]*(l1+1)
    for i in range(1,l1+1):
        for j in range(1,l2+1):
            if s2[j-1] == s1[i-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j]+1,dp[i][j-1]+1,dp[i-1][j-1]+1)
    return dp[l1][l2]

print('编辑距离')
print('The minimum step it will take to modify s1 to s2 is '+ str(manage_dis_rec('horse','ros')))
print(manage_dis_rec_m('horse','ros'))
print(manage_dis_dp('horse','ros'))

#高楼扔鸡蛋问题（不限制鸡蛋个数用二分查找完成)
def binary_search_floor(lissy):
    start = 0
    end = len(lissy)
    while start<end:
        mid = (start+end)//2
        if lissy[mid] == 'P':
            start = mid+1
        if lissy[mid] == 'N':
            end = mid
    if lissy[start] == 'N' and start<len(lissy):
        return start
    else:
        return -1
print('高楼扔鸡蛋')
print(binary_search_floor(['P','P','P','P','N','N','N','N','N']))


#高楼扔鸡蛋问题（限制鸡蛋的个数，用动态规划求解）,较难
def egg_dp(K,N):
    memo = dict()
    def dp(K,N):
        if K == 1: return N
        if N == 0: return 0
        if (K,N) in memo:
            return memo[(K,N)]
        res = float('INF')
        for i in range(1,N+1):
            res = min(res,
                      max(
                          dp(K,N-i),
                          dp(K-1,i-1)
                      )+1 #在第i楼扔一次
                      )
        memo[(K,N)] = res
        return res
    return dp(K,N)
print(egg_dp(2,333))






