

def minimum_bracket_reversal_code(expression):
    if len(expression)%2 == 1:
        return -1
    else:
        stack = []
        min_count = 0
        for x in expression:
            if x == '{':
                stack.append(x)
            elif x == '}' and len(stack) == 0:
                min_count+=1
                stack.append('{')
            elif x == '}' and len(stack)!=0:
                stack.pop()
        return min_count + len(stack)//2
    




if __name__ == '__main__':
    expression = input()
    output = minimum_bracket_reversal_code(expression=expression)
    print(output)