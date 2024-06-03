from optimized_input_taking_of_linkedlist import optimized_input_taking_ll



def print_ith_data(head,index):
    if head is None:
        return -1 
    i = 0
    while head is not None:
        if i==index:
            print(head.data)
            break 
        else:
            i+=1
            head = head.next 




if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    index = int(input())
    head = optimized_input_taking_ll(arr)
    print_ith_data(head,index)