from detailTree import printTree

import sys
sys.setrecursionlimit(3000)
from sys import stdin
class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
    def __str__(self):
        return str(self.data)


def createLevelWiseTree(arr):
    root = treeNode(int(arr[0]))
    q = [root]
    size = len(arr)
    i = 1
    while i<size:
        parent = q.pop(0)
        childCount = int(arr[i])
        i += 1
        for j in range(0,childCount):
            temp = treeNode(int(arr[i+j]))
            parent.children.append(temp)
            q.append(temp)
        i += childCount
    return root




def height_of_tree(tree):
    if tree is None:
        return None 
    height = 1 
    for child in tree.children:
        child_height=height_of_tree(child)
        height = max(height,1+child_height)
    return height





# Main
arr = list(int(x) for x in stdin.readline().rstrip().rsplit())
tree = createLevelWiseTree(arr)


printTree(tree)
height= height_of_tree(tree)
print(height)