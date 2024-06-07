from optimized_input_taking_of_linkedlist import optimized_input_taking_ll, traversal_ll

def eliminate_duplicated_node_in_linked_list(head):
    if head is None:
        return head 
    
    curr = head 
    while curr.next is not None:
        if curr.data == curr.next.data:
            temp = curr.next 
            while temp.next is not None and curr is not None and temp.next.data == curr.data:
                temp = temp.next 
            curr.next = temp.next 
        else:
            curr = curr.next 

    return head 
if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    head = optimized_input_taking_ll(arr)
    output_head = eliminate_duplicated_node_in_linked_list(head)
    traversal_ll(output_head)


"""
Remember to take care of edge case
1 1 
Here at line 11 I did not have temp.next is not None checking so it was giving error NoneType object has not attribute data
To resolve this make sure to check if the temp.next is None if so in else else proceed
"""