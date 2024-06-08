from optimized_input_taking_of_linkedlist import optimized_input_taking_ll


def midpoint_of_linked_list_code(head):
    if head is None:
        return head 
    
    slow = head 
    fast = head 

    while fast.next is not None and fast.next.next is not None:
        fast = fast.next.next 
        slow = slow.next 

    return slow.data


if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    head = optimized_input_taking_ll(arr)
    mid_point = midpoint_of_linked_list_code(head)
    print(mid_point)