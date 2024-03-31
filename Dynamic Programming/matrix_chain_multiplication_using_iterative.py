
def matrix_chain_multiplication(n):
    for i in range(1,n):
        a=1
        b=1
        while b<n:
            b=a+i
            print(a,b,i)
            a+=1
 
if __name__ == '__main__':
    n=4
    matrix_chain_multiplication(n)