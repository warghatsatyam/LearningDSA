from reverse_of_linked_list import generate_reverse_linked_list
from optimized_input_taking_of_linkedlist import optimized_input_taking_ll,traversal_ll
def is_linked_list_palindrome(head):
    fast=head
    slow = head
    while fast is not None and fast.next is not None:
        fast = fast.next.next 
        slow = slow.next 

    second_half = generate_reverse_linked_list(slow)
    first_half = head
    traversal_ll(second_half)
    traversal_ll(first_half)
    while second_half:
        if first_half.data != second_half.data:
            return False
        second_half = second_half.next 
        first_half = first_half.next
    return True





if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    head = optimized_input_taking_ll(arr)
    is_palindrome = is_linked_list_palindrome(head)
    print(is_palindrome)
