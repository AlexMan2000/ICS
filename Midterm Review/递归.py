#回溯算法实现全排列问题(列表中没有重复元素)
def permutation(lissy):
    result = []
    def helper(choosed,toChoose):
        if len(toChoose) == 0:
            result.append(choosed[:])
        for item in toChoose:
            choosed.append(item)
            toChoose.remove(item)
            helper(choosed,toChoose[:])
            choosed.pop()
            toChoose.insert(0,item)
    helper([],lissy)
    return result

print(permutation([1,2,3]))



#递归实现全排列问题（列表中有重复元素）
def permutation_mul(lissy):
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

    size = len(lissy)
    if size == 0:
        return []

    lissy.sort()

    used = [False] * len(lissy)
    res = []
    dfs(lissy, size, 0, [], used, res)
    return res

print(permutation_mul([1,1,2]))



#自底向上的递归(实现列表树)
def maxpath(triangle):
    def helper(i,triangle):
        if i == 0:
            return [17]
        upper = helper(i-1,triangle)
        result = [upper[0]+triangle[i][0]]+[max(upper[j-1]+triangle[i][j],upper[j]+triangle[i][j]) for j in range(1,i)]+[upper[-1]+triangle[i][-1]]
        return result
    return max(helper(len(triangle)-1,triangle))

print(maxpath([[17],[15,8],[5,10,8],[16,6,10,12],[19,10,5,15,12]]))


#自顶向下的递归(实现列表树）
def maxpath_rec(triangle):
    def helper(depth,index):
        if depth == len(triangle)-1:
            return triangle[depth][index]
        return triangle[depth][index] + max(helper(depth+1,index),helper(depth+1,index+1))
    return helper(0,0)

print(maxpath_rec([[17],[15,8],[5,10,8],[16,6,10,12],[19,10,5,15,12]]))



#Tiling problem
def tile_rec(n):
    pass

print(tile_rec(10))