from take_input_tree import takeInput
from detailTree import printTree


def sumOfNodes(root):
    sum = root.data
    for child in root.children:
        sum = sum + sumOfNodes(child)
    return sum 


def checkX(tree,x):
    if tree.data == x:
        return True 
    for child in tree.children:
        if checkX(child,x):
            return True
    return False

if __name__ == '__main__':
    root = takeInput()
    printTree(root=root)
    sum = sumOfNodes(root)
    print(sum)
    is_present = checkX(root,5)
    print(is_present)