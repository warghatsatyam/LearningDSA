from taking_binary_tree_input import treeInput,print_tree

def replace_node_with_depth_code(root,k=0):
    if root is None:
        return
    root.data = k
    replace_node_with_depth_code(root.left,k+1)
    replace_node_with_depth_code(root.right,k+1)


if __name__ == '__main__':
    root = treeInput()
    replace_node_with_depth_code(root)
    print_tree(root)