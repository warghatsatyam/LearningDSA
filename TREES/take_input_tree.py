from detailTree import printTree
from trees import TreeNode

def takeInput():
    print("Enter Root Node Data:")
    rootData = int(input())
    if rootData == -1:
        return 
    root = TreeNode(rootData)
    print("Enter the Number of Children the root node has:")
    childrenCount = int(input())
    for i in range(childrenCount):
        child = takeInput()
        root.children.append(child)
    return root



if __name__ == '__main__':
    root = takeInput()
    printTree(root)