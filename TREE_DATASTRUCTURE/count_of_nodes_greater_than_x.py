from taking_binary_tree_input import treeInput

def count_of_nodes_greater_than_x_in_a_binary_tree(root,x):
    if root is None:
        return 0
    
    left_count = count_of_nodes_greater_than_x_in_a_binary_tree(root.left,x)
    right_count = count_of_nodes_greater_than_x_in_a_binary_tree(root.right,x)

    return (1 if root.data> x else 0) + left_count + right_count




if __name__ == "__main__":
    root = treeInput()
    x = int(input())
    count = count_of_nodes_greater_than_x_in_a_binary_tree(root,x)
    print("Count: ",count)