from taking_binary_tree_input import treeInput,print_tree

def mirror_siblings_position_code(root):
    if root is None:
        return None
    
    if root.left is None and root.right is None:
        return root
    
    root.left.data,root.right.data = root.right.data, root.left.data
    mirror_siblings_position_code(root.left)
    mirror_siblings_position_code(root.right)

    return root



if __name__ == '__main__':
    root = treeInput()
    root = mirror_siblings_position_code(root)
    print_tree(root)