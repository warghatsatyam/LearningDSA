from taking_binary_tree_input import treeInput

def pre_order(root):
    """
    This function print the binary tree in preorder ie left's data then root's data and then right's data
    Args:
        root: This is root of a binary Tree
    Returns:
        This function does not return anythin it only prints the data in preorder way
    """

    if root is None:
        return
    
    print(root.data,end=" ")
    pre_order(root.left)
    pre_order(root.right)


def in_order(root):
    """
    This function print the binary tree in in_order ie left's data then root's data and then right's data
    Args:
        root: This is root of a binary Tree
    Returns:
        This function does not return anythin it only prints the data in in_order way
    """

    if root is None:
        return
    in_order(root.left)
    print(root.data,end=" ")
    in_order(root.right)


def post_order(root):
    """
    This function print the binary tree in postorder ie left's data then root's data and then right's data
    Args:
        root: This is root of a binary Tree
    Returns:
        This function does not return anythin it only prints the data in postorder way
    """

    if root is None:
        return
    post_order(root.left)
    post_order(root.right)
    print(root.data,end=" ")


if __name__ == '__main__':
    root = treeInput()
    print("Preorder")
    pre_order(root)
    print()
    print("Inorder")
    in_order(root)
    print()
    print("Postorder")
    post_order(root)
    print()

