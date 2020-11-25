#最小覆盖子串
def minsubstring(s,t):
    need,window = {},{}

    #遍历t填充目标字典
    for char in t:
        need[char] = need.get(char,0)+1

    #初始化窗口大小和窗口长度,以及用于标记是否满足need的临时变量
    left = right = 0
    #valid记录的是满足条件的字符匹配数，只要窗口中的字符数量大于或者等于need中就算是一个valid数位
    valid = 0

    #记录最小覆盖子串的起始索引终止索引,以及子串的最大长度
    start = 0
    end = 0
    length = float('inf')

    while right < len(s):
        #右边界当前的字符
        curr = s[right]
        #滑动窗口右边界扩充
        right += 1
        if curr in need:
            window[curr] = window.get(curr,0)+1
            if window[curr] == need[curr]:
                valid += 1

        #判断何时应该缩减窗口左边界(可变化)
        while valid == len(need):
            #逻辑判断（可变化)
            if right-left < length:
                start = left
                end = right
                length = end- start

            #开始缩减左边界
            currl = s[left]
            left += 1
            if currl in need:
                if window[currl] == need[currl]:
                    valid -= 1
                window[currl] -= 1

    return s[start:end]



#字符串子串的排列
def stringpermutation(s,t):
    need, window = {}, {}

    # 遍历t填充目标字典
    for char in t:
        need[char] = need.get(char, 0) + 1

    # 初始化窗口大小和窗口长度,以及用于标记是否满足need的临时变量
    left = right = 0
    # valid记录的是满足条件的字符匹配数，只要窗口中的字符数量大于或者等于need中就算是一个valid数位
    valid = 0

    while right < len(s):
        # 右边界当前的字符
        curr = s[right]
        # 滑动窗口右边界扩充
        right += 1
        if curr in need:
            window[curr] = window.get(curr, 0) + 1
            if window[curr] == need[curr]:
                valid += 1

        # 判断何时应该缩减窗口左边界
        while right - left >= len(t):
            #判断返回值逻辑
            if valid == len(need):
                return True

            # 开始缩减左边界
            currl = s[left]
            left += 1
            if currl in need:
                if window[currl] == need[currl]:
                    valid -= 1
                window[currl] -= 1

    return False


#字母异位词(返回所有起始索引),和排列问题很像
def allanagrams(s,t):
    need, window = {}, {}

    for char in t:
        need[char] = need.get(char, 0) + 1

    left = right = valid = 0

    #记录起始索引
    start_list = []

    while right < len(s):
        curr = s[right]
        right += 1
        if curr in need:
            window[curr] = window.get(curr, 0) + 1
            if window[curr] == need[curr]:
                valid += 1

        # 判断何时应该缩减窗口左边界
        while right - left >= len(t):
            # 判断返回值逻辑
            if valid == len(need):
                start_list.append(left)

            currl = s[left]
            left += 1
            if currl in need:
                if window[currl] == need[currl]:
                    valid -= 1
                window[currl] -= 1

    return start_list


#最长无重复子串
def differentsubstring(t):
    window = {}

    left = right = 0

    longest = -float('inf')

    while right < len(t):
        curr = t[right]
        right += 1
        window[curr] = window.get(curr,0)+1
        while window[curr] > 1:
            currl = t[left]
            left += 1
            window[currl] -= 1
        longest = max(longest,right-left)
    return longest



s = 'ADOBECODEBANC'
t = 'ABC'
print("最小覆盖子串: ",minsubstring(s,t))


s1 = 'ab'
s2 = 'eidbaooo'
s21 = 'eidboaoo'
print('字符串排列样例1: ',stringpermutation(s2,s1))
print('字符串排列样例2: ',stringpermutation(s21,s1))


m = 'cbaebabacd'
n = 'abc'
print("字母异位词：",allanagrams(m,n))


t = "abcabcbb"
print("最长无重复子串: ",differentsubstring(t))


