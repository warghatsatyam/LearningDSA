
class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None 

def taking_linkedlist_input_code():
    inputList = [int(item) for item in input().split()]

    head = None
    for currData in inputList:
        if currData == -1:
            break
        newNode = Node(currData)

        if head is None:
            head = newNode
        else:
            curr = head
            while curr.next is not None:
                curr = curr.next
            curr.next = newNode
    return head


def traverse_linked_list(head):
    while head is not None:
        print(head.data)
        head = head.next


if __name__ == '__main__':
    head = taking_linkedlist_input_code()
    traverse_linked_list(head)


