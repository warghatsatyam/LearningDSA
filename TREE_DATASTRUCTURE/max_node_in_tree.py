from taking_binary_tree_input import treeInput

def max_node_in_a_binary_tree(root):
    """
    This function return the max node in a Binary tree
    Args:
        The tree takes as input root node of Binary tree
    Returns:
        The function return's maximum node value in a Binary Tree
    """
    if root is None:
        return -1
    # max node value from left tree
    left_max_node = max_node_in_a_binary_tree(root.left)
    
    # max node value from right tree 
    right_max_node = max_node_in_a_binary_tree(root.right)

    return max(root.data,left_max_node,right_max_node)



if __name__ == '__main__':
    root = treeInput()
    max_node_value = max_node_in_a_binary_tree(root)
    print("Max node value: ",max_node_value)