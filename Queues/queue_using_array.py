class Queue:
    def __init__(self):
        self.__queue = []
        self.__front = 0
        self.__count = 0

    def enqueue(self,data):
         self.__queue.append(data)
         self.__count+=1

    def size_of_queue(self):
        return self.__count 

    def top(self):
        return self.__queue[self.__front]
    
    def dequeue(self):
        if self.__count == 0:
            return -1
        ele = self.__queue[self.__front]
        self.__front+=1
        self.__count-=1
        return ele

    def front(self):
        return self.__queue[self.__front]
    
        
if __name__ == '__main__':
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    print(q.size_of_queue())
    print(q.dequeue())
    print(q.front())
    q.enqueue(3)