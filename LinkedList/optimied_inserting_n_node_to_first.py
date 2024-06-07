from optimized_input_taking_of_linkedlist import optimized_input_taking_ll,traversal_ll


def optimized_insertin_n_node_to_first_code(head, n):
    if head is None and n<=0:
        return head 
    fast = slow = head 

    for _ in range(n):
        if fast.next:
            fast = fast.next 
        else:
            return head 
        
    while fast.next:
        slow = slow.next
        fast = fast.next 

    new_head = slow.next 
    slow.next = None 

    curr = new_head
    while curr.next is not None:
        curr = curr.next 
    curr.next = head 
    return new_head



if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    head = optimized_input_taking_ll(arr)
    n = int(input())
    head = optimized_insertin_n_node_to_first_code(head,n)
    traversal_ll(head)


""" 
say length is 5 and n = 3
and I am using fast and slow pointer technique
so  first I will move fast 3 step ahed while slow stays at start 
Now fast has only 2 step to go
So now I will start moving fast one step and slow one step until fast reaches end

Because only 2 step left for fast slow reaches 2 step ahead and effectively we can break the list here

This is the crux of the fast and slow pointe technique in this problem
"""