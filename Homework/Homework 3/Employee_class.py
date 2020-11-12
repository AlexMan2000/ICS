#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 10:11:08 2017

@author: xg7
"""

class Employee:
    
    def __init__(self, name, id_num, dept, title):
        self.name = name
        self.idnum = int(id_num)
        self.dept = dept
        self.title = title
        
##Alternatively, we can using the following to initilialize
## but in this exercise, we use the above for practice purpose.
#    def __init__(self):
#        self.name = None
#        self.idnum = None
#        self.dept = None
#        self.title = None


    #setter
    ## set_name is an example for setters.
    def set_name(self, name):
        self.name = name
    
    
    #### please complete the following methods
    def set_ID(self, ID):
        # convert ID to an integer when necessary
        self.idnum = int(ID)

    def set_department(self, department):
        self.dept = department

    def set_jobTitle(self, jobTitle):
        self.title = jobTitle
    
    #getter
    ## get_name is an example for getters.
    def get_name(self):
        return self.name
    
    #### please complete the follwing methods
    def get_ID(self):
        return self.idnum
    
    def get_department(self):
        return self.dept
    
    def get_jobTitle(self):
        return self.title


    def __str__(self):
        return "{:<15}|{:<10}|{:<15}|{:<15}".\
            format(self.name,str(self.idnum),self.dept,self.title)

'''
note: 
To get autograded on gradescope, you program can't print anything.

Thus, please comment out the main function call, if you are submitting for auto grading.
'''

'''
if __name__ == '__main__':
    emp1 = Employee("Susan Meyers","47899","Accounting","Vice President")

    ### Please input the information of the rest employees in the table
    print(emp1.get_name(), emp1.get_ID(), emp1.get_department(), emp1.get_jobTitle())
    ### Please complete the following code
    emp2 = Employee("Mark Jones",39119,"IT","Programmer")
    print(emp2.get_name(), emp2.get_ID(), emp2.get_department(), emp2.get_jobTitle())
    emp3 = Employee("Joy Rogers",81774,"Manufacturing","Engineer")
    print(emp3.get_name(), emp3.get_ID(), emp3.get_department(), emp3.get_jobTitle())
'''