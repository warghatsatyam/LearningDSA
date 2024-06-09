from optimized_input_taking_of_linkedlist import optimized_input_taking_ll,traversal_ll

def skip_m_delete_n_code(head,M,N):
    if head is None:
        return head  
    if M == 0:
        return None  
    if N == 0:
        return head 
    
    curr = head
    prev = None  
    
    while curr:
        m = M 
        n = N 
        while m>0 and curr is not None:
            m = m-1 
            prev = curr 
            curr = curr.next
        while n>0 and curr is not None:
            n = n-1
            curr = curr.next
        if prev:
            prev.next = curr 

    return head 


if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    head = optimized_input_taking_ll(arr)
    M = int(input())
    N = int(input())
    head = skip_m_delete_n_code(head,M,N)
    traversal_ll(head)