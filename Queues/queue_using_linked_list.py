class Node:
    def __init__(self,data):
        self.data = data
        self.next = None   

class  Queue:
    def __init__(self):
        self.__queue = None 
        self.__tail = None 
        self.__count = 0

    def enqueue(self,data):
        node = Node(data)
        if self.__queue == None:
            self.__queue = node 
            self.__tail = node
        else:
            self.__tail.next = node 
            self.__tail = node 
        self.__count+=1
    def dequeue(self):
        if self.__count == 0:
            return -1 
        ele = self.__queue
        temp = self.__queue.next 
        self.__queue = temp
        self.__count-=1
        return ele.data 

    def size_of_queue(self):
        return self.__count
    
    def front_of_queue(self):
        if self.__count == 0:
            return -1 
        return self.__queue.data 
    
    def is_empty(self):
        return self.__count == 0
    

if __name__ == '__main__':
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    print(q.size_of_queue())
    print(q.front_of_queue())
    print(q.is_empty())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.front_of_queue())
    print(q.size_of_queue())
    