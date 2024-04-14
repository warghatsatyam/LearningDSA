import queue

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def findLongestPathUtil(root, path, longest_path):
    if root is None:
        return

    # Add the current node to the path
    path.append(root.data)

    # If the current node is a leaf, check if the path is longer than the longest path found so far
    if root.left is None and root.right is None:
        if len(path) > len(longest_path):
            longest_path.clear()
            longest_path.extend(path)

    # Recur for left and right subtrees
    findLongestPathUtil(root.left, path, longest_path)
    findLongestPathUtil(root.right, path, longest_path)

    # Remove the current node from the path before backtracking
    path.pop()

def longestPath(root):
    if root is None:
        return []

    # Variables to store the longest path
    longest_path = []
    current_path = []

    # Find the longest path recursively
    findLongestPathUtil(root, current_path, longest_path)

    return longest_path[::-1]  # Reverse the path to get leaf-to-root order

def buildLevelTree(levelorder):
    index = 0
    length = len(levelorder)
    if length <= 0 or levelorder[0] == -1:
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
            currentNode.left = leftNode
            q.put(leftNode)
        rightChild = levelorder[index]
        index += 1
        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right = rightNode
            q.put(rightNode)
    return root

# Main
levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)
path = longestPath(root)
for ele in path:
    print(ele)
