

def isBalanced(expression):
    open_bracket = ['{','[','(']
    closing_bracket = ['}',']',')']
    arr = []
    for x in expression:
        if x in open_bracket:
            arr.append(x)
        
        elif x in closing_bracket:
            if len(arr) == 0:
                return False
            ele = arr[-1]
            if ele == '{' and x == '}':
                arr.pop()
            elif ele == '[' and x == ']':
                arr.pop()
            elif ele == '(' and x == ')':
                arr.pop()
            else:
                return False

    if len(arr) == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    expression = input()
    print(isBalanced(expression=expression))