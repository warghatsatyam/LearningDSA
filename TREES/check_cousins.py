## Read input as specified in the question.
## Print output as specified in the question.
import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def checkCousins(root, p, q):
    if root is None:
        return False
    
    # Define a function to find the level and parent of a given node
    def findLevelAndParent(node, value, level, parent):
        if node is None:
            return None, None
        
        if node.data == value:
            return level, parent
        
        # Recursively search in the left and right subtrees
        left_level, left_parent = findLevelAndParent(node.left, value, level + 1, node)
        if left_level is not None:
            return left_level, left_parent
        
        right_level, right_parent = findLevelAndParent(node.right, value, level + 1, node)
        return right_level, right_parent
    
    # Find the level and parent of nodes p and q
    p_level, p_parent = findLevelAndParent(root, p, 0, None)
    q_level, q_parent = findLevelAndParent(root, q, 0, None)
    
    # Check if p and q are cousins
    return p_level == q_level and p_parent != q_parent


def buildLevelTree(levelorder):
    index = 0
    length = len(levelorder)
    if length<=0 or levelorder[0]==-1:
        return None
    root = BinaryTreeNode(levelorder[index])
    index += 1
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        currentNode = q.get()
        leftChild = levelorder[index]
        index += 1
        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left =leftNode
            q.put(leftNode)
        rightChild = levelorder[index]
        index += 1
        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right =rightNode
            q.put(rightNode)
    return root

# Main
levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)
p = int(input())
q = int(input())
ans = checkCousins(root,p,q)
if ans is True:
    print('true')
else:
    print('false')
