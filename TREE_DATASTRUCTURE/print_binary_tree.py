from create_binary_tree_node import BinaryTree


def print_tree(root):
    if root is None:
        return
    
    left_data = root.left.data if root.left else -1
    right_data = root.right.data if root.right else -1 
    print(f"{root.data}:-> L:{left_data}, R:{right_data}")

    print_tree(root.left)
    print_tree(root.right)

if __name__ == '__main__':
    node1 = BinaryTree(1)
    node2 = BinaryTree(2)
    node3 = BinaryTree(3)
    node4 = BinaryTree(4)

    node1.left = node2
    node1.right = node3 
    node2.left = node4 

    print_tree(node1)