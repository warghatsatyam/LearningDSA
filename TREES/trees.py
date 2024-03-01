# Generic Tree

class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = list()


node = TreeNode(5)
node1 = TreeNode(2)
node2 = TreeNode(9)
node3 = TreeNode(8)
node4 = TreeNode(7)
node5 = TreeNode(15)
node6 = TreeNode(1)


node.children.append(node1)
node.children.append(node2)
node.children.append(node3)
node.children.append(node4)

node2.children.append(node5)
node2.children.append(node6)

def printTree(root):
    if root == None:
        return 
    
    print(root.data)
    for child in root.children:
        printTree(child)



if __name__ == '__main__':
    printTree(node)




