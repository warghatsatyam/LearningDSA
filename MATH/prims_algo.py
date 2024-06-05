
def print_prime(n):
    prime_num = []
    for i in range(2,n+1):
        is_prime = True 
        for j in range(2,i):
            if i%j == 0:
                is_prime = False 
                break 
        if is_prime:
            prime_num.append(i)
    print(prime_num)

import math

n = 50 
print_prime(n)
        