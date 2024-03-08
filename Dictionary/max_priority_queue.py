class PriorityQueueNode:
    def __init__(self,ele,priority):
        self.ele = ele
        self.priority = priority

class PriorityQueue:
    def __init__(self):
        self.pq = []

    def isEmpty(self):
        #Implement the isEmpty() function here
        return self.getSize()==0
    
    def getSize(self):
        #Implement the getSize() function here
        return len(self.pq)

    def getMax(self):
        #Implement the getMax() function here
        if self.isEmpty():
            return None 
        return self.pq[0].ele
    
    def __percolateUp(self):
        childIndex = self.getSize()-1
        while childIndex>0:
            parentIndex = (childIndex-1)//2
            if self.pq[parentIndex].priority < self.pq[childIndex].priority:
                self.pq[parentIndex],self.pq[childIndex] = self.pq[childIndex],self.pq[parentIndex]
                childIndex=parentIndex
            else:
                break
            
      
    def insert(self,ele,priority):
        #Implement the insert() function here
        pq_node = PriorityQueueNode(ele,priority)
        self.pq.append(pq_node)
        self.__percolateUp()

    def __percolateDown(self):
        parentIndex = 0
        leftIndex = 2*parentIndex+1
        rightIndex = 2*parentIndex+2

        while leftIndex < self.getSize():
            maxIndex = parentIndex
            if self.pq[maxIndex].priority < self.pq[leftIndex].priority:
                maxIndex = leftIndex
            if rightIndex < self.getSize() and self.pq[maxIndex].priority < self.pq[rightIndex].priority:
                maxIndex = rightIndex
            
            if maxIndex == parentIndex:
                break
            self.pq[parentIndex],self.pq[maxIndex]=self.pq[maxIndex],self.pq[parentIndex]
            parentIndex = maxIndex
            leftIndex = 2 * parentIndex+1
            rightIndex = 2 * parentIndex +2
            
        
    def removeMax(self):
        #Implement the removeMax() function here
        if self.isEmpty():
            return None 
        element = self.pq[0].ele
        self.pq[0] = self.pq[self.getSize()-1]
        self.pq.pop()
        self.__percolateDown()
        return element
        
myPq = PriorityQueue()
curr_input = [int(ele) for ele in input().split()]
choice = curr_input[0]
i=1
while choice != -1:
    if choice == 1:
        element = curr_input[i]
        i+=1
        myPq.insert(element,element)
    elif choice == 2:
        print(myPq.getMax())
    elif choice == 3:
        print(myPq.removeMax())
    elif choice == 4:
        print(myPq.getSize())
    elif choice == 5:
        if myPq.isEmpty():
            print('true')
        else:
            print('false')
        break
    else:
        pass
    choice = curr_input[i]
    i+=1