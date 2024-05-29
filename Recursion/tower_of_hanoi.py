

def tower_of_hanoi(n,start,helper,dest):
    if n==1:
        print(f"Move from {start} to {dest}")
    if n>1:
        tower_of_hanoi(n-1,start,dest,helper)
        tower_of_hanoi(1,start,helper,dest)
        tower_of_hanoi(n-1,helper,start,dest)



if __name__ == '__main__':
    tower_of_hanoi(3,'A','B','C')