from trees import TreeNode 
from detailTree import printTree 
from take_input_tree import takeInput


def count_leaf_node(root):
    if root is None:
        return 
    if len(root.children) == 0:
        return 1 
    a = 0 
    for child in root.children:
        x = count_leaf_node(child)
        a+=x
    return a 

if __name__ == '__main__':
    root = takeInput()
    printTree(root=root)
    no_of_leaf_nodes = count_leaf_node(root)
    print("Number of Leaf Nodes are : ", no_of_leaf_nodes)