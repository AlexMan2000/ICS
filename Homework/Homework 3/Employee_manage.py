# -*- coding: utf-8 -*-

from Employee_class import Employee


employees = {}
MENU = """
        -----------------Menu-----------------
        1: Look up an employee
        2: Add a new employee
        3: Change an employee entry
        4: Delete an employee
        5: Quit the program
        --------------------------------------"""

# in case employee's information are already saved to a file, load the information from the file.
def convert_emp_dict():
    with open('emp_database.txt', 'r') as f:
        line = f.readline()
        while line:
            idnum, name, dept, title = line.rstrip('\n').split(',')
            idnum = int(idnum)
            employees[idnum] = Employee(name, idnum, dept, title)
            line = f.readline()


def addEmployee(name,idnum,dept,title):

    if idnum in employees:
        print("An employee with that ID number already exists!")
    else:
        employees[idnum] = Employee(name, idnum, dept, title)


def changeEmployee(idnum,selection,changeTo):

     # NEED TO IMPLEMENT
    if selection == 1:
        employees[idnum].set_name(changeTo)
    elif selection == 2:
        employees[idnum].set_department(changeTo)
    elif selection == 3:
        employees[idnum].set_jobTitle(changeTo)



def deleteEmployee(idnum):
    """
        NEED TO IMPLEMENT THIS FUNCTION
        Given the employee idnum for whom we want to delete from the system,
        delete the employee's info from the system.
        make sure to consider the case when the employee does not exists
        """
    # NEED TO IMPLEMENT
    if idnum in employees:
        del employees[idnum]
    else:
        print('The employee does not exist.')


def searchEmployee(idnum):

    if idnum in employees:
        print("{:<15}|{:<10}|{:<15}|{:<15}".format("Name", "ID Number", "Department", "Job Title"))
        print(employees[idnum])
    else:
        print("Employee not found")


# when user terminates the Employee management system, save the the employee information file 'emp_database.txt'
def saveAndExit():
    """
    NEED TO IMPLEMENT THIS FUNCTION
    after the program ends, user will save the employee data to an outer file "emp_database.txt"
    following required format:
    "ID,name,Department,JobTitle"
    "ID,name,Department,JobTitle"
    ...
    """
    # IMPLEMENT
    output_file = open('emp_database.txt','w')
    for k,v in employees.items():
        output_file.write('{0},{1},{2},{3}\n'.format(k,v.get_name(),v.get_department(),v.get_jobTitle()))
    output_file.close()

'''
note: 
To get autograded on gradescope, you program can't print anything.

Thus, please comment out the main function call, if you are submitting for auto grading.
'''

# def main():
#     status = True
#     convert_emp_dict()
#     while status:
#         print(MENU)
#         selection = int(input("Enter your selection: "))
#         if selection == 1:
#             idnum = int(input("Enter employee ID number: "))
#             searchEmployee(idnum)
#
#         elif selection == 2:
#             name = input("Enter employee name: ")
#             idnum = int(input("Enter employee ID number: "))
#             dept = input("Enter employee department: ")
#             title = input("Enter employee job title: ")
#             addEmployee(name,idnum,dept,title)
#
#         elif selection == 3:
#             idnum = int(input("Enter employee ID number: "))
#             if idnum in employees:
#                 print("What do you want to change?")
#                 print("1: Change name")
#                 print("2: Change department")
#                 print("3: Change job title")
#             selection = int(input("Enter your selection: "))
#             changeTo = input("What do you want to change it to: ")
#             changeEmployee(idnum,selection,changeTo)
#
#         elif selection == 4:
#             idnum = int(input("Enter employee ID number: "))
#             deleteEmployee(idnum)
#
#         elif selection == 5:
#             saveAndExit()
#             status = False
#
#         else:
#             print("Wrong input")
#
#
# if __name__ == '__main__':
#     main()
