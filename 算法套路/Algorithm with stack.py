class ArrayStack:
    ''' Stack implemented with python list append/pop'''
    def __init__(self):
        self.array = []

    def __len__(self):
        return len(self.array)

    def is_empty(self):
        return len(self.array) == 0

    def push(self, e):
        self.array.append(e)

    def top(self):
        if self.is_empty():
            raise Exception("Stack is empty!")
        return self.array[-1]

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty!")
        return self.array.pop(-1)

    def __repr__(self):
        return str(self.array)


#括号匹配简洁写法(无优先级)
def match_parenthesis(s):
    if len(s)%2 == 1:
        return False
    stack = []
    pairs = {')':'('
            ,']':'['
            ,'}':'{'}
    for i in s:
        if i in pairs:
            if not stack or stack.pop() != pairs[i]:
                return False
        else:
            stack.append(i)

    return not stack
# print(match_parenthesis('{(())[]{}}'))



#括号匹配（无数字，有优先级）
def match_pre_parenthesis(s):
    if len(s)%2 == 1:
        return False
    stack = ArrayStack()
    pairs = {')':'('
            ,']':'['
            ,'}':'{'}
    precendence = {'(':1,
                   ')':1,
                   '[':2,
                   ']':2,
                   '{':3,
                   '}':3}
    for i in s:
        if i in pairs:
            if i == ')':
                if stack.top() != '(':
                    return False
                else:
                    stack.pop()
            elif i == ']':
                if stack.top() != '[':
                    return False
                else:
                    stack.pop()
            elif i == '}':
                if stack.top() != '{':
                    return False
                else:
                    stack.pop()
        else:
            if not stack:
                stack.push(i)
            else:
                if precendence[i] > precendence[stack.top()]:
                    return False
                else:
                    stack.push(i)
    return not stack

print(match_pre_parenthesis('{()}')) #True
print(match_pre_parenthesis('{[()]}()')) #True
print(match_pre_parenthesis('{[]()}()')) #True
print(match_pre_parenthesis('([{}])'))  #False
print(match_pre_parenthesis('[{}](){}[]')) #False



#括号匹配(有数字,有优先级)
def match_num_parenthesis(s):
    stack = ArrayStack()
    operand_stack = ArrayStack()
    pairs = {')':'('
            ,']':'['
            ,'}':'{'}
    precendence = {'(':1,
                   ')':1,
                   '[':2,
                   ']':2,
                   '{':3,
                   '}':3}
    for i in s:
        if i.isnumeric():
            operand_stack.push(i)
        else:
            if i in pairs:
                if i == ')':
                    if stack.top() != '(':
                        return False
                    else:
                        stack.pop()
                elif i == ']':
                    if stack.top() != '[':
                        return False
                    else:
                        stack.pop()
                elif i == '}':
                    if stack.top() != '{':
                        return False
                    else:
                        stack.pop()
            else:
                if not stack:
                    stack.push(i)
                else:
                    if precendence[i] > precendence[stack.top()]:
                        return False
                    else:
                        stack.push(i)
    return not stack
print(match_num_parenthesis('{3(9)8}')) #True



#定义计算器
def calculate(num1,op,num2):
    if op == '*':
        return eval(num1)*eval(num2)
    elif op == '+':
        return eval(num1)+eval(num2)
    elif op == '-':
        return eval(num1)-eval(num2)
    elif op == '/':
        return eval(num1)/eval(num2)



#数学表达式（无括号）
def match_expression_simple(s):
    operator_stack = ArrayStack()
    operand_stack = ArrayStack()
    precendence = {'*':3,'/':2,'+':1,'-':1}
    for curr in s:
        if curr.isnumeric():
            operand_stack.push(curr)
        else:
            while operator_stack and precendence[operator_stack.top()] >= precendence[curr]:
                num2 = operand_stack.pop()
                op = operator_stack.pop()
                num1 = operand_stack.pop()
                result = calculate(num1,op,num2)
                operand_stack.push(str(result))
            operator_stack.push(curr)
    while operator_stack:
        num2 = operand_stack.pop()
        op = operator_stack.pop()
        num1 = operand_stack.pop()
        result = str(calculate(num1,op,num2))
        operand_stack.push(result)
    return operand_stack.top()
# print(match_expression_simple('3+9*2-3'))


#数学表达式（有括号）
def match_expression(s):
    operator_stack = ArrayStack()
    operand_stack = ArrayStack()
    precendence = {'*':3,'/':3,'+':2,'-':2,'(':1,')':1}
    for curr in s:
        if curr.isnumeric():
            operand_stack.push(curr)
        if curr == '(':
            operator_stack.push(curr)
        if curr == ')':
            while operator_stack.top()!='(':
                num2 = operand_stack.pop()
                op = operator_stack.pop()
                num1 = operand_stack.pop()
                result = str(calculate(num1,op,num2))
                operand_stack.push(result)
            operator_stack.pop()
        if curr in '+-/*':
            while operator_stack and precendence[operator_stack.top()]>=precendence[curr]:
                num2 = operand_stack.pop()
                op = operator_stack.pop()
                num1 = operand_stack.pop()
                result = str(calculate(num1,op,num2))
                operand_stack.push(result)
            operator_stack.push(curr)
    while operator_stack:
        num2 = operand_stack.pop()
        op = operator_stack.pop()
        num1 = operand_stack.pop()
        result = str(calculate(num1,op,num2))
        operand_stack.push(result)
    return operand_stack.top()
# print(match_expression("9 + 8 * ( 7 - 6 ) / ( 2 / 8 )"))  #41
# print(match_expression("9 + 8 * 7 / ( 6 + 5 ) - ( 4 + 3 ) * 2"))  # 0.0909090909
# print(match_expression("9 + 8 * 7 / ( ( 6 + 5 ) - ( 4 + 3 ) * 2 )")) # -9.66666666667