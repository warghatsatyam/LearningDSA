
from optimized_input_taking_of_linkedlist import optimized_input_taking_ll

def find_node_in_linked_list_recursively_code(head,n): 
    if head is None:
        return -1 
    if head.data == n:
        return 0 
    index = find_node_in_linked_list_recursively_code(head.next, n)
    if index == -1:
        return -1 
    return 1+index


if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    head = optimized_input_taking_ll(arr)
    n = int(input())
    index = find_node_in_linked_list_recursively_code(head,n)
    print(index)

    
