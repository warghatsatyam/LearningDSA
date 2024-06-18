from taking_binary_tree_input import treeInput,print_tree


def height(root):
    if root is None:
        return 0 
    return 1 + max(height(root.left), height(root.right))



def is_binary_tree_balanced_code(root):
    """
    This function return boolean value indicating whether the given tree is balanced or not 
    Args:
        root: This is root of the binary Tree 
    Returns:
        boolean: This function return true/false indication whether the tree is balanced or not 
    """
    if root == None:
        return True
    
    hl = height(root.left)
    hr = height(root.right)

    if hl-hr>1 or hr-hl>1:
        return False
    
    is_left_balanced = is_binary_tree_balanced_code(root.left)
    is_right_balanced = is_binary_tree_balanced_code(root.right)

    if is_left_balanced and is_right_balanced:
        return True
    else:
        return False
    

if __name__ == '__main__':
    root = treeInput()
    print_tree(root)
    print(is_binary_tree_balanced_code(root))