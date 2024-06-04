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

def insertin_node_at_ith_index(head,data,index):
    new_node = Node(data)

    # If inserting at head of the linked list
    if index == 0:
        new_node.next = head 
        return new_node

    #If the list is empty return -1
    if head is None:
        return -1
         
    prev = None 
    curr = head 
    pos = 0

    # Traversing the list until the desired position
    while pos!=index and curr is not None:
        prev = curr 
        curr = curr.next 
        pos+=1

    # If the index is greater than the position ie greater than the length of the linked list return -1
    if pos!=index:
        return -1 
    
    # Else Insert the new node at given index position
    prev.next = new_node
    new_node.next = curr 
    
    return head


if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    head = optimized_input_taking_ll(arr)
    data = int(input("Enter the Node Value: "))
    index = int(input("Enter the index where to insert the new node: "))
    head = insertin_node_at_ith_index(head,data,index)
    traverse_linked_list(head)