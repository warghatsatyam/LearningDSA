from optimized_input_taking_of_linkedlist import optimized_input_taking_ll

def length_of_linkedlist_iteratively(head):
    length = 0
    curr = head
    while curr is not None:
        length+=1
        curr = curr.next 
    return length


if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    head = optimized_input_taking_ll(arr)
    length = length_of_linkedlist_iteratively(head)
    print(length)