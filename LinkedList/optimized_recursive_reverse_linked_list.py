from optimized_input_taking_of_linkedlist import optimized_input_taking_ll,traversal_ll

def recursive_reverse_linked_list(head):
    if head is None or head.next is None:
        return head,head
    
    new_head,tail = recursive_reverse_linked_list(head.next)
    tail.next = head
    head.next = None 
    return new_head,head



if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    head = optimized_input_taking_ll(arr)
    reverse_head,tail = recursive_reverse_linked_list(head)
    traversal_ll(reverse_head)