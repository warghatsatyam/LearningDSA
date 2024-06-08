
from optimized_input_taking_of_linkedlist import optimized_input_taking_ll,traversal_ll

def generate_reverse_linked_list(head):
    prev = None
    current = head 

    while current is not None:
        next_node = current.next 
        current.next = prev 
        prev = current
        current = next_node

    return prev
    

if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    head = optimized_input_taking_ll(arr)
    reverse_head = generate_reverse_linked_list(head)
    traversal_ll(reverse_head)