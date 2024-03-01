from take_input_tree import takeInput 
from detailTree import printTree 

def get_sum(tree_node_list):
    sum_node = 0
    for x in tree_node_list:
        sum_node+=x.data
    return sum_node

def max_sum_node(root):
    if root is None:
        return None 
    parent_node = root
    max_sum = get_sum(root.children)
    for child in root.children:
        node,sum_node = max_sum_node(child)
        if sum_node> max_sum:
            max_sum = sum_node
            parent_node = node
        # parent_node = node
    return parent_node,max_sum



if __name__ == '__main__':
    root = takeInput() 
    printTree(root)
    node,node_sum = max_sum_node(root)
    print(node.data)