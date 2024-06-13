class Queue:
    def __init__(self):
        self.__stack1 = []
        self.__stack2 = []
        self.__size = 0

    def enqueue(self,data):
        self.__stack1.append(data)
        self.__size+=1

    def dequeue(self):
        if self.__size == 0:
            return -1
        else:
            while len(self.__stack1) >1:
                ele = self.__stack1.pop()
                self.__stack2.append(ele)
            ele  = self.__stack1.pop()

            while len(self.__stack2):
                tmp = self.__stack2.pop()
                self.__stack1.append(tmp)
        self.__size-=1
        return ele 
    
    def size_of_stack(self):
        return self.__size
    
    def is_empty(self):
        return self.__size == 0
    


if __name__ == '__main__':
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    q.enqueue(6)
    print(q.size_of_stack())
    print(q.is_empty())
    print(q.dequeue())
    print(q.dequeue())
    print(q.size_of_stack())
    print(q.is_empty())

    

