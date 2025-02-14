def is_balanced_parentheses(s):
    ''' # basuraaaa
    parentheses = 0
    brackets = 0
    braces = 0

    for i in s:
        if -1 in [parentheses, brackets, braces]: return False

        if i == '(':
            parentheses +=1
        elif i == '[':
            brackets += 1
        elif i == '{':
            braces += 1

        elif i == ')':
            parentheses -=1
        elif i == ']':
            brackets -= 1
        elif i == '}':
            braces -= 1

    return parentheses == brackets == braces == 0
    '''
    stack = []

    try:
        for i in s:
            if i in ['(', '[', '{']: 
                stack.append(i)
                continue
            
            if stack[-1] == '(':
                if i == ')':
                    stack.pop()
                    continue
                else: 
                    return False
            
            if stack[-1] == '[':
                if i == ']':
                    stack.pop()
                    continue
                else:
                    return False
            
            if stack[-1] == '{':
                if i == '}':
                    stack.pop()
                    continue
                else:
                    return False
    except:
        return False
    
    return len(stack) == 0
    



print(is_balanced_parentheses('(()){}'))