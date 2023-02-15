stack = []
operators = ('+', '-', '*', '/', '^', '(', ')')

prefix = ['6', '+', '3', '*', '(', '1', '+', '4', '*', '5', ')' '*', '2']
postfix = []


for char in prefix:
    if char in operators:
        stack.append(char)
        if stack[-1] == ')':
            while stack[-1] != '(':
                postfix.append(stack.pop())
            postfix.pop()
        elif stack[-1]:
            pass
