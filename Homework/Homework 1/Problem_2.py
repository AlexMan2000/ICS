#Judge if the number is prime or not
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
