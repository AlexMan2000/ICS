

# define a function cut_robe

def cut_robe(n):
    total = 1
    dp = [0]*(n+1)
    dp[2] = 2
    dp[3] = 3
    for i in range(2,n+1):
        for j in range(1,i):
            tmp = max(j,dp[j])*max(i-j,dp[i-j])
            dp[i] = max(dp[i],tmp)
    total = dp[-1]
    return total


print('cut a robe of length 8, the resulting value is {}'.format(cut_robe(8)))

