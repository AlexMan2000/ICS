num = int(input('Please enter a number'))
while num < 0:
    num = int(input('You entered a negative number, please enter a non-negative one'))
#Using list to save time complexity
output_list = []
while num >= 1000:
    num -= 1000
    output_list.append('M')
if num >= 900:
    num -= 900
    output_list.append('CM')
if 500 <= num < 900:
    num -= 500
    output_list.append('D')
if 400 <= num < 500:
    num -= 400
    output_list.append('CD')
if 100 <= num < 400:
    while num >= 100:
        num -= 100
        output_list.append('C')
if num >= 90:
    num -= 90
    output_list.append('XC')
if 50 <=num < 90:
    num -= 50
    output_list.append('L')
if 40 <=num < 50:
    num -= 40
    output_list.append('XL')
if 10 <= num < 40:
    while num >= 10:
        num -= 10
        output_list.append('X')
if num == 9:
    output_list.append('IX')
if 5 <= num < 9:
    num -= 5
    output_list.append('V')
if 4<= num < 5:
    num -= 4
    output_list.append('IV')
if num < 4:
    while num > 0:
        num -= 1
        output_list.append('I')
print(''.join(output_list))



