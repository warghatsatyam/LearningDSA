from length_of_ll_recursive import recursive_linked_list_length
from optimized_input_taking_of_linkedlist import optimized_input_taking_ll,traversal_ll


def append_n_nodes_to_first_code(head,n):
    length_of_linked_list = recursive_linked_list_length(head)
    new_length = n-length_of_linked_list

    count = 0
    curr  = head 
    while count<new_length:
        count+=1
        print(count)
        curr = curr.next 
    new_head = curr.next 

    # This will break the node in two part 1 to n-1 and  n to N
    curr.next = None 

    curr = new_head
    while curr.next is not None:
        curr = curr.next 
    curr.next = new_head
    return new_head


if __name__  == '__main__':
    arr = [int(x) for x in input().split()]
    head = optimized_input_taking_ll(arr)
    n = int(input())
    new_head = append_n_nodes_to_first_code(head,n)
    traversal_ll(new_head)

