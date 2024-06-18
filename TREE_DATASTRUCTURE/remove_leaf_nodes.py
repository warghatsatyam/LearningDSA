from taking_binary_tree_input import treeInput,print_tree


def remove_leaf_nodes_of_tree(root):
    if root is None:
        return 
    if root.left is None and root.right is None:
        return None
    
    root.left  = remove_leaf_nodes_of_tree(root.left)
    root.right = remove_leaf_nodes_of_tree(root.right)
    return root

if __name__ == '__main__':
    root = treeInput()
    root = remove_leaf_nodes_of_tree(root)
    print_tree(root)