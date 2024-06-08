from optimized_input_taking_of_linkedlist import optimized_input_taking_ll,traversal_ll

def merge_linked_list(h1,h2):
    if h1 is None:
        return h2 
    if h2 is None:
        return h1 
    if h1 is None and h2 is None:
        return None 
    
    ft,fh = None,None 
    if h1.data < h2.data:
        ft,fh = h1,h1
        h1 = h1.next 
    else:
        ft,fh = h2 
        h2 = h2.next 

    while h1 is not None and h2 is not None:
        if h1.data < h2.data:
            ft.next = h1 
            ft = h1 
            h1 = h1.next 
        else:
            ft.next = h2 
            ft = h2 
            h2 = h2.next 
    
    if h1 is not None:
        ft.next = h1 
    
    if h2  is not None:
        ft.next = h2 

    return fh


if __name__ == '__main__':
    arr1 = [int(x) for x in input().split()]
    arr2 = [int(x) for x in input().split()]

    h1 = optimized_input_taking_ll(arr1)
    h2 = optimized_input_taking_ll(arr2)

    head = merge_linked_list(h1, h2)
    traversal_ll(head)