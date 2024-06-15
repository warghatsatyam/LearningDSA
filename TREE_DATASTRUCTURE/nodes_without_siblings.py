from taking_binary_tree_input import treeInput

def nodes_without_siblings(root):
    """
    This functions print those nodes which do not have siblings
    Args:
        root: The function takes root node as input
    Return:
        The function return nothing. It simply print nodes without siblings
    """

    if root is None:
        return
    
    if root.left is None and root.right is not None:
        print(root.right.data, end=" ")
    if root.right is None and root.left is not None:
        print(root.left.data, end=" ")
    
    nodes_without_siblings(root.left)
    nodes_without_siblings(root.right)




if __name__ == '__main__':
    root = treeInput()
    nodes_without_siblings(root)