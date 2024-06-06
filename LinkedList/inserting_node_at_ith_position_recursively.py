from optimized_input_taking_of_linkedlist import optimized_input_taking_ll,traversal_ll

class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None 


def inserting_node_at_ith_position_recursively_code(head,data,i):
    if head is None:
        return None 
    if i == 0:
        new_node = Node(data)
        new_node.next = head 
        return new_node 

    smaller_linked_list_head  = inserting_node_at_ith_position_recursively_code(head.next,data,i-1)
    head.next = smaller_linked_list_head
    return head


if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    head = optimized_input_taking_ll(arr)
    data = int(input())
    index = int(input())
    new_head = inserting_node_at_ith_position_recursively_code(head,data,index)
    traversal_ll(head)