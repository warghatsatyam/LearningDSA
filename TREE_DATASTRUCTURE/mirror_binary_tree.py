from taking_binary_tree_input import treeInput,print_tree

def mirror_binary_tree_code(root):
    if root is None:
        return 
    
    if root.left is None and root.right is None:
        return 
    
    if root.left is None:
        root.left = root.right 
        root.right = None 

    if root.right is None:
        root.right = root.left 
        root.left = None

    if root.left is not None and root.right is not None:
        root.left,root.right = root.right,root.left
        mirror_binary_tree_code(root.left)
        mirror_binary_tree_code(root.right)



if __name__ == '__main__':
    root = treeInput()
    mirror_binary_tree_code(root)
    print_tree(root)