# Loay Mohamed
# Challeng 2:

exp = input("Input string to be evaluated:")
#exp = "(1+2)+(2+7)"
stack = []

for char in exp:
    if char == '(' or char == '+' or char == '-':
        stack.append(char)
    elif char == ')':
        # get the index of '('
        index = len(stack)-1
        while stack[index] != '(':
            index -= 1
        enter = False
        while stack[-1] != '(':
            #case (-num)
            if stack[index] == '(' and stack[index+1] == '-':
                num = int(stack.pop(index+2))
                stack.pop()  # pop '-'
                stack.pop()  # pop '(')
                stack.append(str(-1*num))
                break
            if not enter:
                index += 1
                enter = True
            x = int(stack.pop(index))
            if stack[-1] == '(':
                stack.pop()
                stack.append(str(x))
                break
            else:
                oper = stack.pop(index)
                y = int(stack[index])
                if oper == '+':
                    stack[index] = (str(x+y))
                else:  # oper == '-'
                    stack[index] = (str(x-y))

    elif char == ' ':
        pass
    else:
        stack.append(char)

if len(stack) > 1:
    index = 0
    while len(stack) > 1:
        x = int(stack.pop(index))
        if len(stack) == 1 and stack[-1] == '(':
            stack.pop()
            stack.append(str(x))
            break
        else:
            oper = stack.pop(index)
            y = int(stack[index])
            if oper == '+':
                stack[index] = (str(x+y))
            else:  # oper == '-'
                stack[index] = (str(x-y))
print(stack.pop())
