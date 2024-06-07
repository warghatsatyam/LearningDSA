from optimized_input_taking_of_linkedlist import optimized_input_taking_ll,traversal_ll


def optimized_insertin_n_node_to_first_code(head, n):
    if head is None and n<=0:
        return head 
    fast = slow = head 

    for _ in range(n):
        if fast.next:
            fast = fast.next 
        else:
            return head 
        
    while fast.next:
        slow = slow.next
        fast = fast.next 

    new_head = slow.next 
    slow.next = None 

    curr = new_head
    while curr.next is not None:
        curr = curr.next 
    curr.next = head 
    return new_head



if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    head = optimized_input_taking_ll(arr)
    n = int(input())
    head = optimized_insertin_n_node_to_first_code(head,n)
    traversal_ll(head)