from create_binary_tree_node import BinaryTree


def print_tree(root):
    if root is None:
        return -1 
    if root.left is not None and root.right is not None:
        print(f"{root.data}:->L:{root.left.data},R:{root.right.data}")
        print_tree(root.left)
        print_tree(root.right)
    elif root.left is not None and root.right is None:
        print(f"{root.data}:->L:{root.left.data},R:{-1}")
        print_tree(root.left)
    elif root.left is None and root.right is not None:
        print(f"{root.data}:->L:{-1},R:{root.right.data}")
        print_tree(root.right)
    else:
        print(f"{root.data}:->L:{-1},R:{-1}")



if __name__ == '__main__':
    node1 = BinaryTree(1)
    node2 = BinaryTree(2)
    node3 = BinaryTree(3)
    node4 = BinaryTree(4)

    node1.left = node2
    node1.right = node3 
    node2.left = node4 

    print_tree(node1)