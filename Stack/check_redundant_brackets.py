

def check_redundant_brackets_code(expression):
    stack = []
    for x in expression:
        if x == ')':
            count = 0
            while stack.pop()!='(':
                count+=1
            if count<=1:
                return True
        else:
            stack.append(x)
    return False


if __name__ == '__main__':
    expression = input()
    print(check_redundant_brackets_code(expression))