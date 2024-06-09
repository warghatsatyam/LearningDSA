from optimized_input_taking_of_linkedlist import optimized_input_taking_ll,traversal_ll

def even_after_odd_code(head):
    if head is None:
        return head 
    curr = head  
    eh,et,oh,ot = None,None,None,None 
    while curr is not None:
        if curr.data % 2 == 0:
            if eh is None:
                eh,et = curr,curr 
                curr = curr.next 
            else:
                et.next = curr
                et = curr 
                curr = curr.next
        else:
            if oh is None:
                oh,ot = curr,curr
                curr = curr.next 
            else:
                ot.next = curr 
                ot = curr 
                curr = curr.next 
    if oh is not None:
        ot.next = eh 
        if et is not None:
            et.next = None
        return oh
    return eh

if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    head = optimized_input_taking_ll(arr)
    output_head = even_after_odd_code(head)
    traversal_ll(output_head)
