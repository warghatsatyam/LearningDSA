from taking_linkedlist_input import taking_linkedlist_input_code



def recursive_linked_list_length(head):
    if head is None:
        return 0 
    return 1 + recursive_linked_list_length(head.next)


if __name__ == '__main__':
    head = taking_linkedlist_input_code()
    length_of_ll = recursive_linked_list_length(head)
    print("Length of LL", length_of_ll)