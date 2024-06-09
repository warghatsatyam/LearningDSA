
from optimized_input_taking_of_linkedlist import traversal_ll,optimized_input_taking_ll


def midpoint_of_linked_list(head):
    if head is None:
        return head 
    if head.next is None:
        return head 
    
    slow = head
    fast = head 

    while fast.next is not None and fast.next.next is not None:
        fast = fast.next.next 
        slow = slow.next 

    return slow

def merge_linked_list(h1,h2):
    if h1 is None:
        return h2 
    if h2 is None:
        return h1 
    ft,fh = None,None
    if h1.data < h2.data:
        ft,fh = h1,h1
        h1 = h1.next 
    else:
        ft,fh = h2,h2
        h2 = h2.next

    while h1 is not None and h2 is not None:
        if h1.data < h2.data:
            ft.next = h1 
            ft = h1 
            h1 = h1.next
        else:
            ft.next = h2 
            ft = h2 
            h2 = h2.next 
    
    if h1:
        ft.next = h1 
    if h2:
        ft.next = h2 
    return fh


def merge_sort(head):
    if head is None:
        return head 
    
    if head.next is None:
        return head 
    
    mid_point = midpoint_of_linked_list(head)
    
    new_list = mid_point.next
    mid_point.next = None

    h1 = merge_sort(head)
    h2 = merge_sort(new_list)
    fh = merge_linked_list(h1,h2)
    return fh




if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    head = optimized_input_taking_ll(arr)
    output_head = merge_sort(head)
    traversal_ll(output_head)
