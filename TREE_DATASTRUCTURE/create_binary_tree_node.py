
class BinaryTree:
    def __init__(self,data):
        self.data  = data 
        self.left  = None 
        self.right = None 

    
if __name__ == '__main__':
    node1 = BinaryTree(1)
    node2 = BinaryTree(2)
    node3 = BinaryTree(3)
    node4 = BinaryTree(4)

    node1.left = node2
    node1.right = node3 
    node2.left = node4 

    print(node1.data)
    print(node1.left.data)
    print(node1.right.data)
    print(node2.left.data)