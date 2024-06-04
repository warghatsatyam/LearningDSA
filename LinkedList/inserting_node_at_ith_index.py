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
    newNode = Node(data)
    if head is None and index == 0:
        return newNode
    if head is not None and index == 0:
        newNode.next = head 
        head = newNode
        return head 
    prev = None 
    curr = head 
    pos = 0
    while pos!=index and curr is not None:
        prev = curr 
        curr = curr.next 
        pos+=1

    if pos!=index:
        return -1 
    else:
        prev.next = newNode
        newNode.next = curr 
    return head


if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    head = optimized_input_taking_ll(arr)
    data = int(input("Enter the Node Value: "))
    index = int(input("Enter the index where to insert the new node: "))
    head = insertin_node_at_ith_index(head,data,index)
    traverse_linked_list(head)