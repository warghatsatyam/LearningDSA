
from optimized_input_taking_of_linkedlist import optimized_input_taking_ll,traversal_ll

def generate_reverse_linked_list(head):
    if head is None:
        return head 
    
    if head.next is None:
        return head 
    
    reverse_head = generate_reverse_linked_list(head.next)
    reverse_head.next = head 
    return reverse_head
    

if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    head = optimized_input_taking_ll(arr)
    reverse_head = generate_reverse_linked_list(head)
    traversal_ll(reverse_head)