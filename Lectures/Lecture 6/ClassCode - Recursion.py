#斐波那契数列低效递归
def fib(n):
    if n<2:
        return n
    return fib(n-1)+fib(n-2)
print(fib(4))


#斐波那契数列高效递归(记忆化储存）
def fib_m(n):
    def helper(n,memo={}):
        if n<2:
            return n
        try:
            return memo[n]
        except KeyError:
            result = fib_m(n-1) + fib_m(n-2)
            memo[n] = result
            return result
    return helper(n)
print(fib_m(4))



#斐波那契数列迭代




#最小距离(O(n^2))




#最小距离(O(nlogn))




#最小距离(O(n))




#Powerset(函数内递归)




#Powerset(本体递归)




#快速排序(递归, 时间复杂度O(nlogn),空间复杂度O(nlogn))
def quicksort(lissy):
    if len(lissy) <= 1:
        return lissy
    low,pivot,high = segment(lissy)
    return quicksort(low)+[pivot]+quicksort(high)

def segment(seq):
    pivot,seq = seq[0],seq[1:]
    low = []
    high = []
    for i in seq:
        if i>= pivot:
            low.append(i)
        else:
            high.append(i)
    return low,high,pivot

#快速排序(指针交换，空间复杂度O(1))










#Picking the few bill(贪心算法)






#Picking the few bills(动态规划)
def pick_bills(coins,amount):
    # dp = [amount+1]*len(amount+1)
    pass









print(pick_bills([9,6,5,1],11))

#Picking the few bills(递归)
def pick_bils_rec(lissy,target):
    pass




print(pick_bils_rec([9,6,5,1],11))




#列表树的最大路径(类比帕斯卡三角形
def maxpath(triangle):
    def helper(i,triangle):
        if i == 0 :
            return [17]
        upper = helper(i-1,triangle)
        result = [upper[0]+triangle[i][0]]+[max(upper[j-1]+triangle[i][j],upper[j]+triangle[i][j]) for j in range(1,i)]+[upper[-1]+triangle[i][-1]]
        return result
    return max(helper(len(triangle)-1,triangle))

print(maxpath([[17],[15,8],[5,10,8],[16,6,10,12],[19,10,5,15,12]]))



#Pancake sorting
#烧饼排序



#Number Placement(Recursion)
#求得每一种排列，分别验证


#Site selection(Smallest distance)
#数学公式法





#Tiling problems





#Anagram detection(recursion)



#Steam_stale(最大背包问题)
def steam_stale(game_size,value,W):
    #定义dp数组
    #dp[i][W]表示，前[1.....i]个游戏，最大背包容量为W时的最大价值
    dp = [[0]*(W+1)]*(len(game_size)+1)
    for i in range(1,len(game_size)+1):
        for W in range(W+1):
            if W-game_size[i-1] < 0:
                dp[i][W] = dp[i-1][W]
            else:
                dp[i][W] = max(dp[i-1][W],dp[i-1][W-game_size[i-1]]+value[i-1])

    return dp[-1][W]






print(steam_stale([10,15,10,2,5,1],[190,300,180,20,35,10],20))
