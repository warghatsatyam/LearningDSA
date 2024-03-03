class MapNode:
    def __init__(self,key,value):
        self.key = key 
        self.value = value 
        self.next = None 

class Map:
    def __init__(self):
        self.bucketSize=3
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
        head = self.buckets[index]
        newNode = MapNode(key,value)
        newNode.next = head 
        self.buckets[index] = newNode
        self.count+=1
        loadFactor = self.count/self.bucketSize
        if loadFactor >=0.7:
            self.rehash()


    def search(self,key):
        hc = hash(key)
        index = self.getBucketIndex(hc)
        head = self.buckets[index]
        while head is not None:
            if head.key == key:
                return head.value
            head=head.next
        return None
    
    def rehash(self):
        temp = self.buckets
        self.buckets = [None for i in range(2*self.bucketSize)]
        self.bucketSize = 2*self.bucketSize
        self.count = 0 
        for head in temp:
            while head is not None:
                self.insert(head.key,head.value)
                head = head.next
            
    
    def remove(self,key):
        hc = hash(key)
        index = self.getBucketIndex(hc)
        head = self.buckets[index]
        prev = None 
        while head is not None:
            if head.key == key:
                self.count-=1
                if prev is None:
                    self.buckets[index] = head.next
                else:
                    prev.next = head.next 
                return head.value 
            prev = head 
            head = head.next
        return None 
    
if __name__ == '__main__':
    m = Map()
    m.insert('Satyam',2)
    print(m.count)
    print("bucketsize",m.bucketSize)
    m.insert('Luffy',6)
    print(m.count)
    print("bucketsize",m.bucketSize)
    m.insert('chetan',6)
    print(m.count)
    print("bucketsize",m.bucketSize)
    m.insert('a',6)
    print(m.count)
    print("bucketsize",m.bucketSize)
    m.insert('b',6)
    print(m.count)
    print("bucketsize",m.bucketSize)
    m.insert('c',6)
    print(m.count)
    print("bucketsize",m.bucketSize)
    m.insert('d',6)
    print(m.count)
    print("bucketsize",m.bucketSize)
    
    
    