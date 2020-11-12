#Exercise 2
def missingNumber(lissy):
    lissy.sort()
    i = 0
    while i < len(lissy):
        if i!= lissy[i]:
            return i

#Exercise 3
import re
class Person:
    def __init__(self,name,age,phone_number):
        self._name = name
        self._age = age
        if re.match(r'1[2|3|5|7|8]\d{9}$',phone_number):
            self._phoneNumber = phone_number
        else:
            print('%s,the format of your phone number is wrong. Please update it afterwards'%(self._name))

    def getter(self):
        return self.__dict__

    def mutate(self,value):
        print('What do you want to change?')
        print('1 ---- name, str')
        print('2 ---- age, int')
        print('3 ---- phonenumber, str')
        choice = int(input('Please make a choice between 1-3'))
        if choice == '1':
            self._name = value
        elif choice == '2' :
            if isinstance(value,int):
                self._age = value
            else:
                print('Unable to update your age, since you input a string')
        else:
            if re.match(r'1[2|3|5|7|8]\d{9}$', value):
                self._phoneNumber = value
            else:
                print('%s,the format of your phone number is still wrong. Please update it afterwards' % (self._name))



# person1 = Person('Jack',23,'138166368112')
# person2 = Person('Mary',24,'15023102031')
#
# person1.mutate('123123123')
# print(person1.getter())


#Exercise 4
import random
test = dict([('Alaska','Juneau'),('Arizona','Phoenix'),('Arkansas','Little Rock')])
count = 0
print('Do you want to start')
print('1 ---- yes')
print('0 ---- no')
res = int(input(''))
while res != 0:
    num = random.randint(0,len(test)-1)
    correct = test[list(test.keys())[num]]
    print('Please give the answer to this province: %s'%list(test.keys())[num])
    answer = input()
    if correct == answer:
        print('It is right!')
        count += 1
    else:
        print('Your answer is wrong, would you like to try again')
        print('1 ---- yes')
        print('0 ---- no')
        res = int(input(''))
print('You have made %s answer(s) correct'% count)




#Exercise 5
# text_1 = open('text_one.txt','r')
# text_2 = open('text_two.txt','r')
# word_1 = text_1.read()
# word_2 = text_2.read()
# total_string = word_1+' '+word_2
# word_list = total_string.split(' ')
# for i in range(len(word_list)):
#     word_list[i] = word_list[i].strip(',')
# a = dict()
# for i in word_list:
#     if i.isalpha():
#         a[i] = a.get(i,0)+1
# output_list=[]
# print(a)
# for i in a.keys():
#     if a[i] > 1:
#         output_list.append(i)
# final_sting = ' '.join(output_list)
# new_file = open('text_three.txt','w')
# new_file.write(final_sting)

