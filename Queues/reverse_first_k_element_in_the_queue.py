import queue
from queue import Queue,LifoQueue

from reverse_queue import reverse_queue_code, print_queue,queue_input

def reverse_first_k_element(qu,k):
    reverse_queue_code(qu)
    n = qu.qsize()
    stack = LifoQueue()
    i=0
    while i< n-k:
        ele = qu.get()
        stack.put(ele)
        i+=1
    while stack.qsize()!=0:
        ele = stack.get()
        qu.put(ele)

    return qu

if __name__ == '__main__':
    qu = queue_input()
    k = int(input())
    output_qu = reverse_first_k_element(qu,k)   
    print_queue(output_qu)