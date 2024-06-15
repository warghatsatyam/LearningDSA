from taking_binary_tree_input import treeInput

def print_node_at_depth_k(root,k):
    if root is None:
        return -1
    
    if k==0 and root is not None:
        print(root.data,end=" ")
    print_node_at_depth_k(root.left,k-1)
    print_node_at_depth_k(root.right,k-1)


if __name__ == '__main__':
    root = treeInput()
    k = int(input("Depth: "))
    print_node_at_depth_k(root,k)
    print()
    