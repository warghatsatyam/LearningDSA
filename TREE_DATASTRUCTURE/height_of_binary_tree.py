from taking_binary_tree_input import treeInput 

def height_of_binary_tree_code(root):
    if root is None:
        return 0
    left = height_of_binary_tree_code(root.left)
    right = height_of_binary_tree_code(root.right)
    return 1 + max(left,right)


if __name__ == '__main__':
    root = treeInput()
    height_of_tree = height_of_binary_tree_code(root)
    print(height_of_tree)