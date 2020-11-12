"""
Checks expressions for matching brackets – "()"s, "[]"s and "{}"s
"""

import stack_student as sk
"""
Algorithm:
Scan along the string:
        when meets an opening bracket, push it into the stack.
        when meets a closing bracket,

            if it stack top is the paired opening bracket, 
                     pop the top, 

           else:
                   return False
when finish scanning, if the stack is empty, return True, else return False
"""

brackets = { ']':'[', ')':'(', '}':'{' }

def brackets_balance(exp):
    """exp represents the expression"""
    stack = sk.Stack()
    for i in exp:
        if i in brackets:
            if stack.is_empty() or stack.peek() != brackets[i]:
                return False
            else:
                stack.pop()
        else:
            if i in '[({':
                stack.push(i)

    return stack.is_empty()




def main():

    expList = ["(..)...(..)", \
               "(...)...(..", \
               ")...(...(...)", \
               "[...(...)...]", \
               "[...(...]...)"]

    for e in expList:
        print(brackets_balance(e))

main()
