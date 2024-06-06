from optimized_input_taking_of_linkedlist import optimized_input_taking_ll,traversal_ll

class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None 


def delete_node_at_ith_index_recursively_code(head,index):
    if index<0:
        return None
    if head is None:
        return None 
    if index==0:
        return head.next 
    smaller_linked_list_head = delete_node_at_ith_index_recursively_code(head.next,index-1)
    head.next = smaller_linked_list_head
    return head 


if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    head = optimized_input_taking_ll(arr)
    index = int(input())
    new_head = delete_node_at_ith_index_recursively_code(head,index)
    traversal_ll(head)