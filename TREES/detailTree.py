from trees import TreeNode,node




def printChildren(root):
    for child in root.children:
        print(child.data , end=' ')


def printTree(root):
    if root == None:
        return 
    print(root.data,end=':')
    for child in root.children:
        print(child.data,end=' ')
    print()
    for child in root.children:
        printTree(child)

if __name__ == '__main__':
    printTree(node)