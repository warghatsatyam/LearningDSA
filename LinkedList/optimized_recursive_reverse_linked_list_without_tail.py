from optimized_input_taking_of_linkedlist import optimized_input_taking_ll,traversal_ll

def recursive_reverse_linked_list_without_tail(head):
    if head is None or head.next is None:
        return head
    
    new_head = recursive_reverse_linked_list_without_tail(head.next)
    if new_head.next is None:
        new_head.next = head 
        head.next = None 
    else:
        head.next.next = head 
        head.next = None 
    return new_head



if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    head = optimized_input_taking_ll(arr)
    reverse_head= recursive_reverse_linked_list_without_tail(head)
    traversal_ll(reverse_head)