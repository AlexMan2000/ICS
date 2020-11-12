num = int(input('Please enter a non-negative number'))
#Justify the input
while num < 0:
    print('You input a negative number, please enter a positive number.')
    num = int(input('Please enter a non-negative number'))
output = 1
#The judgement on zero is optional since 0! = 1, which does not affect the overall output
for i in range(1,num+1):
    output *= i
print(output)
