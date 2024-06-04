from optimized_input_taking_of_linkedlist import optimized_input_taking_ll


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 

def traverse_linked_list(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next
    print()

def delete_node_at_ith_index_code(head,index):
    
    #If head is None return None
    if head is None:
        return head 
    
    #If deleting first element
    if index == 0:
        curr = head 
        head = head.next 
        curr.next = None 
        return head 

    # traversing to the index
    prev = None 
    curr = head 
    pos = 0
    while pos<index and curr is not None:
        prev = curr 
        curr = curr.next 
        pos+=1
    
    # index is greater than length of linked list
    if pos!=index:
        return None 

    #Deleting element at ith index
    prev.next = curr.next 
    curr.next = None 
    return head 


if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    head = optimized_input_taking_ll(arr)
    index = int(input("Enter the index where to delete the node: "))
    head = delete_node_at_ith_index_code(head,index)
    traverse_linked_list(head)