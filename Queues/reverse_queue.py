import queue

def queue_input():
    n = int(input())
    qu = queue.Queue()

    for i in range(n):
        value = int(input())
        qu.put(value)

    return qu 


def reverse_queue_code(qu):
    if qu.qsize() <= 1:
        return qu 
    else:
        ele = qu.get()
        reverse_queue_code(qu)
        qu.put(ele)
        return qu

def print_queue(qu):
    n = qu.qsize()
    for _ in range(n):
        print(qu.get(), end=" ")

if __name__ == '__main__':
    qu = queue_input()
    output_qu = reverse_queue_code(qu)
    print_queue(output_qu)
    

""" 
In order to do the reversal process inplace we are not returning anything
we are directly performing operation on the same queue
hence in the else block there is no varible to capture return value

"""