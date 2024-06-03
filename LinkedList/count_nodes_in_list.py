from optimized_input_taking_of_linkedlist import optimized_input_taking_ll

def count_nodes(head):
    if head is None:
        return 0
    count = 0
    while head is not None:
        count+=1
        head = head.next 
    return count 


if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    head = optimized_input_taking_ll(arr)
    count = count_nodes(head)
    print(count)

