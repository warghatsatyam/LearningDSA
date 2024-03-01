from take_input_tree import takeInput
from detailTree import printTree

def numNodes(root):
    if root == None:
        return 
    count = 1
    for child in root.children:
        count+=numNodes(child)
    return count




if __name__ == '__main__':
    root = takeInput()
    printTree(root=root)
    count = numNodes(root)
    print(count)