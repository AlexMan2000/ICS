#Exercise 1
def perks(num):
    return 0.22*num

#Exercise 2
def func(num):
    if 10 <= num <= 19:
        return num*99*0.9
    elif 20<= num <= 49:
        return num*99*0.8
    elif 50<= num <= 99:
        return num*99*0.7
    else:
        return num*99*0.6

#Exercise 3
def FizzBuzz():
    for i in range(100):
        if i%3 == 0 and i%5 == 0:
            print('Fizz')
        elif i%5 == 0 and i%3 == 0:
            print('Buzz')
        elif i%3 ==0 and i%5 == 0:
            print('FizzBuzz')


#Exercise 4
def draw():
    for i in range(5):
        print('*'*i)
    for i in range(4,-1,-1):
        print('*'*i)


#Exercise 5
def is_prime(num):
    for i in range(2,num):
        if num%i == 0:
            print('Not Prime')
    print('Prime')
    


