from trees import TreeNode
from detailTree import printTree
import queue

def input_level_wise():
    q = queue.Queue()
    print("Enter the Root:")
    rootData = int(input())
    if rootData == -1:
        return None 
    
    rootNode = TreeNode(rootData)
    q.put(rootNode)
    while (not q.empty()):
        current_node = q.get()
        print("Number of child Nodes of", current_node.data)
        no_of_child = int(input())
        for i in range(no_of_child):
            print("Enter the child Node", current_node.data)
            childData = int(input())
            childNode = TreeNode(childData)
            current_node.children.append(childNode)
            q.put(childNode)
    return rootNode




if __name__=='__main__':
    root = input_level_wise()
    printTree(root)