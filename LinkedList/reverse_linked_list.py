from optimized_input_taking_of_linkedlist import optimized_input_taking_ll,traversal_ll

def reverse_linked_list_code(head):
    if head is None:
        return
    reverse_linked_list_code(head.next)
    print(head.data, end=" ")



if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    head = optimized_input_taking_ll(arr)
    reverse_linked_list_code(head)
