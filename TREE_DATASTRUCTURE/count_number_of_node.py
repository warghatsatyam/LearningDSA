from taking_binary_tree_input import treeInput


def count_number_of_nodes_in_binary_tree(root):
    """ 
    Return count of the number of nodes in a binary tree
    Args:
        root (TreeNode): The root node of the Binary Tree
    Returns:
        int: The number of nodes in the Binary Tree
    """

    if root is None:
        return 0
    
    left_tree_node_count = count_number_of_nodes_in_binary_tree(root.left)
    right_tree_node_count = count_number_of_nodes_in_binary_tree(root.right)
    return 1 + left_tree_node_count + right_tree_node_count


if __name__ == '__main__':
    root = treeInput()
    count_of_nodes = count_number_of_nodes_in_binary_tree(root)
    print("Count of Number of Nodes is : ",count_of_nodes)