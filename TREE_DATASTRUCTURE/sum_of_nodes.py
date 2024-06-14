from taking_binary_tree_input import treeInput

def sum_of_nodes_in_a_binary_tree(root):
    """
    This function takes the input root of binary tree as input and return sum of all the nodes in a binary tree
    Args:
        root: This is root of a binary tree
    Returns:
        sum(int): Return sum of  all the nodes in  a binary tree.
    """

    if root is None:
        return 0
    left_tree_sum = sum_of_nodes_in_a_binary_tree(root.left)
    right_tree_sum = sum_of_nodes_in_a_binary_tree(root.right)
    return root.data + left_tree_sum + right_tree_sum

if __name__ == '__main__':
    root = treeInput()
    sum_of_nodes = sum_of_nodes_in_a_binary_tree(root)
    print("Sum: ",sum_of_nodes)