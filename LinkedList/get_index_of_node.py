from optimized_input_taking_of_linkedlist import optimized_input_taking_ll
def get_index_of_node_code(head,data):
    if head is None:
        return -1 
    is_present = False
    pos = 0
    while head is not None:
        if head.data == data:
            is_present = True
            break
        else:
            pos+=1
            head = head.next 
    if is_present:
        return pos 
    return -1 


if __name__  == '__main__':
    arr = [int(x) for x in input().split()]
    head = optimized_input_taking_ll(arr)
    data = int(input())
    node_position = get_index_of_node_code(head, data)
    if node_position!=-1:
        print(f"The node  {data} is present at index {node_position}")
    else:
        print(f"The node {data} is not present")