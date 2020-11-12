def namesearch(name):
    """
    :param name: String -- name entered by the user. 
    :return: True if name appears in either girl's name list or boy's name list
             False if otherwise
    """	
    # to do
    boys = open('BoyNames.txt','r')
    girls = open('GirlNames.txt','r')
    boys_list = boys.read().split('\n')
    girls_list = girls.read().split('\n')
    boys.close()
    girls.close()
    if name in boys_list or name in girls_list:
        return True
    else:
        return False

'''
note: 
To get autograded on gradescope, you program can't print anything.

Thus, please comment out the main function call, if you are submitting for auto grading.
'''



# def main():
#     print (namesearch('Dylan'))   # Expected output: True
#     print (namesearch('Emily'))   # Expected output: True
#     print (namesearch('James'))    # Expected output: True
#     print (namesearch('God'))   # Expected output: False
#     print (namesearch('Vic'))     # Expected output: False
#
#
#
# if __name__ == '__main__':
#     main()
