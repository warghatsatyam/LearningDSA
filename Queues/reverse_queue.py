import queue

def queue_input():
    n = int(input())
    qu = queue.Queue()

    for i in range(n):
        value = int(input())
        qu.put(value)

    return qu 


if __name__ == '__main__':
    qu = queue_input()
    