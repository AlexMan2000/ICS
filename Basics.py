#回溯算法解决全排列
def callpermutation(lst):
    def permutation(choosed,toChoose):
        if len(toChoose) == 0:
            print(choosed)
        for i in toChoose:
            #从选择列表中移除
            choosed.append(i)
            toChoose.remove(i)
            #递归,注意这里传入切片即可避免后续对于字列表元素的修改
            permutation(choosed,toChoose[:])
            #将选择撤销
            choosed.pop()
            toChoose.insert(0,i)
    permutation([],lst)

callpermutation([1,2,3])


#回溯算法解决所有子集
def subsets(nums):
    res = []
    n = len(nums)

    def backtrack(i, tmp):
        # 注意这里一定要用列表的引用，否者后面更新temp会改变res中元素的值
        res.append(tmp[:])
        for j in range(i, n): #函数在函数体内找不到n时，回去上级函数体内找，最终找到最初定义的N的值
            tmp.append(nums[j])
            backtrack(j + 1, tmp)
            tmp.pop()

    backtrack(0, [])
    return res


# print(subsets([1,2,3]))

def call_num(n):
    print('I will need',n,'numbers')
    import math
    shortest = math.inf
    longest = -math.inf
    shortest_str = None
    longest_str = None
    for i in range(1,n+1):
        userinput = input('Word No. {}'.format(i))
        if len(userinput) <= shortest:
            shortest_str = userinput
            shortest = len(userinput)
        if len(userinput) >= longest:
            longest_str = userinput
            longest = len(userinput)
    print('Shortest_word',shortest_str)
    print('Longest_word',longest_str)
    print('Average',(shortest+longest)/2)


def kthGrammar(N, K):
    def helper(N):
        if N == 1:
            return '0'
        tmp = helper(N - 1)
        lissy=[]
        for i in range(len(tmp)):
            lissy.append(tmp[i])
        for i in range(len(lissy)):
            if lissy[i] == '0':
                lissy[i] = '01'
            else:
                lissy[i] = '10'
        return ''.join(lissy)
    print(helper(3))
    return helper(N)[K - 1]


def triangle(N):
    if N == 0:
        return []
    if N == 1:
        return [1]
    upper = triangle(N-1)
    return [1]+[upper[i]+upper[i-1] for i in range(1,N-1)]+[1]

def func(n):
    k = 1
    while k*k < n:
        if n%k == 0:
            yield k
            yield n//k
        k+=1
    if k * k == n:
        yield k

print([i for i in func(100)])


def tester(nums,target):
    result = []
    n = len(nums)
    def backtrack(i, tmp):
        # 注意这里一定要用列表的引用，否者后面更新temp会改变res中元素的值
        if sum(tmp) == target:
            result.append(tmp[:])
            return
        for j in range(i, n): #函数在函数体内找不到n时，回去上级函数体内找，最终找到最初定义的N的值
            tmp.append(nums[j])
            backtrack(j + 1, tmp)
            tmp.pop()

    backtrack(0,[])
    return result

lissy = [1,2,3,4,7,8]
target = 8
result = tester(lissy,target)
print(result)


# t = [[0]*3]*4
# t[0][2] =2
# print(t)
# a = [[]]*3
# for i in range(3):
#     a[i] = ['....']
# print(a)
# print(id(a[0]),id(a[1]),id(a[2]))

# b = [['....']]*3
# print(b)
# print(id(b[0]),id(b[1]),id(b[2]))

# print([1]*3)

def func(*args):
    print(*args)
    print(args)

func(1,2,3)


def pick_bills(coins,target):
    dp = [target+1]*(target+1)
    dp[0] = 0
    for i in range(len(dp)):
        for coin in coins:
            if i-coin<0:
                continue
            else:
                dp[i] = min(dp[i],1+dp[i-coin])
    return dp[target] if dp[target]!=target else -1

#
# print(pick_bills([9,6,5,1],11))
# print(pick_bills([9,7,1,20],24))
# print(pick_bills([9,6,5,6],35))

def maximum_sum(lissy):
    #定义dp
    dp = [0]*len(lissy)
    for i in range(len(lissy)):
        dp[i] = max(dp[i-1]+lissy[i],lissy[i])
    return max(dp)

# print(maximum_sum([-2,1,-3,4,-1,2,1,5,5,6,-5,4]))
a = [(2,5),(3,4),(3,2)]
a.sort(key = lambda k:k[0])
a.sort(key = lambda k:k[1])
print(a)


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


print(binary_search_floor(['P','P','P','P','N','N','N','N','N']))



#for k,v in list的用法, 这种用法适用于一个可迭代对象，且这个可迭代对象中含有诸如(1,2),[1,2],{1,2}这样的键值对，
#才可用for k,v in list来遍历数据。
a = [{1,2},{5,6},{8,4}]
for k,v in a:
    print(k,v)



#enumerate函数的用法
a = [[1,2,3],[3,2,4],[5,6,3]]
for i,v in enumerate(a[0]):
    print(i,v)


import random
a = [6,3,2,5,4]
t = random.randint(0,len(a)-1)
print(t)
a[0],a[t] = a[t],a[0]
print(a)
print(a[t])

a = [1,2,2,2,2]
a.insert(-1,10)
print(a)
#
#
import pickle
a = {'a':1,'b':2,'q':3}
newfile = open('tester.txt','wb')
pickle.dump(a,newfile)
newfile.close()

extract = open('tester.txt','rb')
ob = pickle.load(extract)
print(ob)

a = 'VIII alexbob?!'
print(a[2:None])

class A:
    def __init__(self,value):
        self.value = value

    def __add__(self, other):
        return A(self.value+other.value)

    def __str__(self):
        return str(self.value)

#定义完__add__函数之后,__iadd会按照__add__函数的模式来计算.
a = A(3)
b = A(4)
a += b
print(a)


import numpy
lissy = numpy.arange(20,50)
print(lissy)

a = [(2,3),(3,4)]
for m,(n,t) in enumerate(a):
    print(m,n,t)

(t,q) = (2,3)
print(t,q)

a = [1,2,3]
b = [2,3,4]
t = list(zip(a,b))
print(t)


t = open('tester2.txt','w')
for i in range(100):
    t.write(str(i)+'\n')
t.close()
lines2 = []
lines3 = []
m = open('tester2.txt','r')
lines = m.readlines()
# lines2+=m.read().split('\n')
lines3+=lines
# print(lines2)
print(lines3)
m.close()

a = {'a':2,'b':3}
print(sorted(a,key = a.get,reverse = True))


a = [1,2,3]
b = [1,2,3]
print(a == b)

a = "asw\n"
print(a.strip())
print(2)

print((((8-4)/2)*((3+1)+2))-(3*(7-2)+1))

t = [1,2,3]
m = '123'
# print(m.index("4"))

print(type(ord("A")))
print(m.replace('1','2'))
print(m)
