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
