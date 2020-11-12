def reverseVowel(s):
    if s == '':
        return ''
    vowel_list = ['a','e','i','o','u']
    string_list = list(s)
    left = 0
    right = len(s)-1
    flag_left = True
    flag_right = True
    while left < right:
        if s[left] not in vowel_list:
            left += 1
            flag_left = False
        else:
            flag_left = True
        if s[right] not in vowel_list:
            right-=1
            flag_right = False
        else:
            flag_right = True
        if flag_left and flag_right:
            string_list[left],string_list[right] = string_list[right],string_list[left]
            left+=1
            right-=1
    return ''.join(string_list)

