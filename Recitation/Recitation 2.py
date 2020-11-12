def max():
    n1 = int(input('Please enter the first number'))
    n2 = int(input('Please entr the second number'))
    n_out = 0
    if n1 < n2:
        n_out = n2
    elif n1 > n2:
        n_out = n1
    elif n1 == n2:
        print('The two numbers are equal')
        return
    print('The bigger of the two numbers is {}'.format(n_out))


s = 'John William Smith'
def exercise2(s):
    string_list = list(s)
    output_list = []
    for i in string_list:
        output_list.append(i[0])
    return '.'.join(output_list)+'.'



def exercise3(num):
    string = str(num)
    start = 0
    end = len(string)-1
    while start < end:
        if string[start] != string[end]:
            return False
        start += 1
        end -= 1
    return True


def exercise4(lissy,num):
    cur = 0
    for i in range(len(lissy)):
        if lissy[i] == num:
            lissy.pop(i)
    return lissy



def exercise5():
    dictionary = dict((i,{}) for i in range(2011,2016))
    dictionary[2011]['Derrick Rose'] = 'Dallas Mavericks'
    dictionary[2012]['LJ'] = 'MH'
    dictionary[2013]['LJ'] = 'MH'
    dictionary[2014]['KD'] = 'SAS'
    dictionary[2015]['SC'] = 'GSW'
    return dictionary


#O(n)
def challenge(num):
    if num == 1:
        return [[1]]
    upper = challenge(num-1)
    upper.append([1]+[(upper[-1][i]+upper[-1][i-1]) for i in range(1,num-1)]+[1])
    return upper

output_list = challenge(5)
for i in output_list:
    for j in i:
        print(j,end='')
    print()


#O(n^2)
def challenge2(num):
    pass


