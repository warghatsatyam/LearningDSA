class Node:
    def __init__(self,data):
        self.data = data 
        self.next = next  


class Stack:
    def __init__ (self):
        self.__head = None
        self.__count = 0 

    def push(self,data):
        node = Node(data)
        if self.__head is None:
            self.__head = node 
        else:
            node.next = self.__head 
            self.__head = node 
        self.__count+=1
    
    def pop(self):
        if self.__count == 0:
            raise 'Stack is already Empty'
        else:
            ele = self.__head
            self.__head = self.__head.next
            self.__count-=1
            return ele.data 
        
    def top(self):
        if self.__count == 0:
            return 'Stack is Empty'
        else:
            return self.__head.data
        
    def isEmpty(self):
        return self.__count == 0
    
    def size_of_stack(self):
        return self.__count
    


