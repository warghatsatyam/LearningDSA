from take_input_tree import takeInput

from detailTree import printTree 

def replacewithDepthHelper(tree,d):
    tree.data = d 
    for child in tree.children:
        replacewithDepthHelper(child,d+1)
    

def replacewithDepth(tree):
    if tree is None:
        return 
    replacewithDepthHelper(tree,d=0)


if __name__ == '__main__':
    tree = takeInput()
    replacewithDepth(tree)
    printTree(tree)