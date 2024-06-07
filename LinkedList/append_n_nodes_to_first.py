from optimized_input_taking_of_linkedlist import optimized_input_taking_ll,traversal_ll
from length_of_ll_iteratively import length_of_linkedlist_iteratively

def append_n_nodes_to_first_code(head,n):
    length_of_linked_list = length_of_linkedlist_iteratively(head)
    new_length = length_of_linked_list-n

    if head is None or n<=0:
        return head
    
    if new_length <=0:
        return head
    
    count = 0
    curr  = head 
    while count<new_length-1:
        count+=1
        curr = curr.next
    new_head = curr.next 

    # This will break the node in two part 1 to n-1 and  n to N
    curr.next = None 

    curr1 = new_head
    while curr1.next is not None:
        curr1 = curr1.next 
    curr1.next = head
    return new_head


if __name__  == '__main__':
    arr = [int(x) for x in input().split()]
    head = optimized_input_taking_ll(arr)
    n = int(input())
    new_head = append_n_nodes_to_first_code(head,n)
    traversal_ll(new_head)

