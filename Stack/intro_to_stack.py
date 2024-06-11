class Stack:
    def __init__(self):
        self.__arr = []
        self.size = len(self.__arr)

    def push(self,data):
        self.__arr.append(data)
        self.size+=1

    def pop(self):
        ele = self.__arr.pop()
        self.size-=1
        return ele 
    
    def size_of_stack(self):
        return self.size
    
    def isEmpty(self):
        return self.size == 0
    
    def top(self):
        ele = self.__arr[self.size -1 ]
        return ele 
    
if __name__ == '__main__':
    s = Stack()
    s.push(10)
    s.push(11)
    s.push(12)
    s.push(13)
    s.push(14)
    print(s.size_of_stack())
    print(s.top())
    print(s.isEmpty())
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.size_of_stack())

