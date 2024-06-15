from taking_binary_tree_input import treeInput

def is_node_present_in_a_binary_tree(root,x):
    """
    This function check if the given node is present in a binary tree
    Args:
        root: This is root node of a binary tree
        x   : This is node whose present is checked in the Tree
    Return:
        boolean: This return true or false
    """
    if root is None:
        return False
    if root.data == x:
        return True
    is_present_in_left = is_node_present_in_a_binary_tree(root.left,x)
    is_present_in_right = is_node_present_in_a_binary_tree(root.right,x)

    if is_present_in_left or is_present_in_right:
        return True
    else:
        return False
    


if __name__ == '__main__':
    root = treeInput()
    x = int(input("Node: "))
    is_present = is_node_present_in_a_binary_tree(root,x)
    print(is_present)