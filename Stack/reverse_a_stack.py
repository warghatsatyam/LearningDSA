

def reverse_a_stack_code(inputStack,extraStack):
    if len(inputStack) <=1:
        return
    
    while len(inputStack)!=1:
        ele = inputStack.pop()
        extraStack.append(ele)
    element = inputStack.pop()
    while len(extraStack)!=0:
        ele = extraStack.pop()
        inputStack.append(ele)
    reverse_a_stack_code(inputStack,extraStack)
    inputStack.append(element)

if __name__ == '__main__':
    inputStack = [1,2,3,4,5]
    extraStack = []
    reverse_a_stack_code(inputStack,extraStack)
    print(inputStack)