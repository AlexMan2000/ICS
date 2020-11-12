#Problem 1
def draw():
    for i in range(6):
        print('*{0}*'.format(' '*i))


#Problem 2
def PNL():
    #O(n^2)
    def is_prime(num):
        if not isinstance(num,int):
            print('Please enter an integer.')
        ret = True
        if num == 1:
            ret= False
        elif num < 3:
            ret= True
        for i in range(2, num//2+1):
            if num % i == 0:
                ret = False
                break
        return ret
    for i in range(1,101):
        if is_prime(i):
            print(i)
        else:
            continue

#Problem 3
def Factorial():
    num = int(input('Please enter a non-negative number'))
    #Justify the input
    while num < 0:
        print('You input a negative number, please enter a positive number.')
        num = int(input('Please enter a non-negative number'))
    output = 1
    for i in range(1,num+1):
        output *= i
    print(output)


#Problem 4
def Wheel_Color():
    num = int(input('Please input a non-negative integer'))
    if num<0 or num>36:
        print('Error! The inputed value is out of range')
    else:
        if num == 0:
            print('The No.{0} pocket is green'.format(num))
        elif 1<= num <=10 or 19 <= num <= 28:
            if num % 2 != 0:
                print('The No.{0} pocket is red'.format(num))
            else:
                print('The No.{0} pocket is black'.format(num))
        else:
            if num %2 == 0:
                print('The No.{0} pocket is red'.format(num))
            else:
                print('The No.{0} pocket is black'.format(num))



#Problem 5
def Zodiac():
    year = int(input('Please enter a year number'))
    while year < 0:
        year = int(input('Please enter an AC year'))
    #Corresponding zodiac starts from the year number that can be divided by 12 (e.g. 2004 // 12 = 167 , 'Monkey').
    zodiac_list = ['Monkey','Rooster','Dog','Pig','Rat','Ox','Tiger','Hare','Dragon','Snake','Horse','Sheep']
    print('Year {0} is the year of {1}'.format(year,zodiac_list[year%12]))



def main():
    draw()
    PNL()
    Factorial()
    Wheel_Color()
    Zodiac()


main()