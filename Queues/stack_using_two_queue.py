

class StackUsingTwoQueue:
    def __init__(self):
        self.__queue1 = []
        self.__queue2 = []
        self.__size   = 0
        self.__front1  = 0
        self.__front2  = 0
        
    def push(self,data):
        self.__queue1.append(data)
        self.__size+=1 

    def pop(self):
        if self.__size == 0:
            return -1
        while self.__front1 < len(self.__queue1)-1:
            ele = self.__queue1[self.__front1]
            self.__front1+=1
            self.__queue2.append(ele) 
        ele = self.__queue1.pop()

        while self.__front2 <len(self.__queue2):
            tmp = self.__queue2[self.__front2]
            self.__front2+=1
            self.__queue1.append(tmp)
        
        self.__size-=1
        return ele 
    
    def top(self):
        if self.__size == 0:
            return -1 
        
        while self.__front1 < len(self.__queue1) - 1:
            ele = self.__queue1[self.__front1]
            self.__front1+=1
            self.__queue2.append(ele)
        ele = self.__queue1.pop()

        while self.__front2 < len(self.__queue2):
            tmp = self.__queue2[self.__front2]
            self.__front2+=1
            self.__queue1.append(tmp)

        self.__queue1.append(ele)
        return ele
    
    def get_size(self):
        return self.__size
    
    def is_empty(self):
        return self.__size == 0 

if __name__  == '__main__':
    sq = StackUsingTwoQueue()
    sq.push(1)
    print("top",sq.top())
    sq.push(2)
    print("top",sq.top())
    sq.push(3)
    print("top",sq.top())
    print(sq.get_size())
    print("Pop",sq.pop())
    print("top",sq.top())
    print(sq.get_size())
    print("Pop",sq.pop())
    print("top",sq.top())
    print(sq.get_size())
    print("top",sq.top())
