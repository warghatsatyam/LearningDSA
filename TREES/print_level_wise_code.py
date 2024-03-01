from detailTree import printTree 
from input_levelwise_code import input_level_wise
import queue

def print_level_wise(root):
    tree_string = ''
    if root is None:
        return None 
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        current_node = q.get()
        print(current_node.data, end=':')
        tree_string+=str(current_node.data)
        child_node_arr = current_node.children
        num_children = len(child_node_arr)
        for i, x in enumerate(child_node_arr):
            print(x.data, end='')
            if i < num_children - 1:
                print(',', end='')
            q.put(x)
        print()
    print(tree_string)



if __name__ == '__main__':
    root = input_level_wise()
    print_level_wise(root)
    