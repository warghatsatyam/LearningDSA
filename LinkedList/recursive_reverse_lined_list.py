from optimized_input_taking_of_linkedlist import optimized_input_taking_ll,traversal_ll

def recursive_reverse_linked_list(head):
    if head is None:
        return head
    if head.next is None:
        return head 
    
    new_head = recursive_reverse_linked_list(head.next)
    curr = new_head
    while curr.next is not None:
        curr = curr.next 

    curr.next = head 
    head.next = None 
    return new_head



if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    head = optimized_input_taking_ll(arr)
    reverse_head = recursive_reverse_linked_list(head)
    traversal_ll(reverse_head)