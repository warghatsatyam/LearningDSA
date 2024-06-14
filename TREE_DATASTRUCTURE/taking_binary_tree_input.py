from print_binary_tree import print_tree

class BinaryTreeNode:
    def __init__(self,data):
        self.data = data 
        self.left = None 
        self.right = None 



def treeInput():
    root_data = int(input())
    if root_data == -1:
        return None 
    root_node = BinaryTreeNode(root_data)
    left_tree = treeInput()
    right_tree = treeInput()
    root_node.left = left_tree
    root_node.right = right_tree
    return root_node


if __name__ == '__main__':
    root = treeInput()
    print_tree(root=root)

    