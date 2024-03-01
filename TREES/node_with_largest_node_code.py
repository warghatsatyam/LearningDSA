from detailTree import printTree 
from take_input_tree import takeInput 


def node_with_largest_data(tree):
    if tree is None:
        return None 
    max_node = tree.data 
    for child in tree.children:
        max_child_node = node_with_largest_data(child)
        if max_child_node > max_node:
            max_node = max_child_node 
    return max_node


if __name__ == '__main__':
    tree = takeInput()
    printTree(tree)
    max_node = node_with_largest_data(tree)
    print(max_node)



