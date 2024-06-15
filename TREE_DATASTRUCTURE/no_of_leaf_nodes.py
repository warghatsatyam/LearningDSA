from taking_binary_tree_input import treeInput

def no_of_leaf_nodes_in_tree(root):
    if root.left is None and root.right is None:
        return 1 
    left = no_of_leaf_nodes_in_tree(root.left)
    right = no_of_leaf_nodes_in_tree(root.right)
    return left+right


if __name__ == '__main__':
    root = treeInput()
    count_of_leaf_nodes = no_of_leaf_nodes_in_tree(root)
    print("Leaf Nodes Count",count_of_leaf_nodes)