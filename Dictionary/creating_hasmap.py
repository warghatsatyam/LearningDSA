class MapNode:
    def __init__(self,key,value):
        self.key = key 
        self.value = value 
        self.next = None 

class Map:
    def __init__(self):
        self.bucketSize=10  
        self.buckets = [None for x in range(self.bucketSize)]
        self.count = 0


    def size(self):
        return self.count
    
    def getBucketIndex(self,hc):
        return (abs(hc)%self.bucketSize)

    def insert(self,key,value):
        hc = hash(key)
        index = self.getBucketIndex(hc)
        head = self.buckets[index]
        while head is not None:
            if head.key == key:
                head.value = value 
                return 
            head = head.next 
        newNode = MapNode(key,value)
        newNode.next = head 
        self.buckets[index] = newNode
        self.count+=1



if __name__ == '__main__':
    m = Map()
    m.insert('Satyam',2)
    print(m.count)
    m.insert('Luffy',6)
    print(m.count)
    m.insert('Satyam',6)
    print(m.count)