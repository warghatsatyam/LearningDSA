class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 



def optimized_input_taking_ll(arr):
    head = None 
    for ele in arr:
        node = Node(ele)

        if head is None:
            head = node 
            curr = head 
        else:
            curr.next = node 
            curr = curr.next 
    return head 


def traversal_ll(head):
    curr = head 
    while curr is not None:
        print(curr.data)
        curr = curr.next
    

if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    head = optimized_input_taking_ll(arr)
    traversal_ll(head)