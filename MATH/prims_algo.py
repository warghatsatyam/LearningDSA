import math 
def print_prime(n):
    prime_num = []
    for i in range(2,n+1):
        is_prime = True 
        for j in range(2,math.ceil(math.sqrt(n))):
            if i%j == 0 and i!=j:
                is_prime = False 
                break 
        if is_prime:
            prime_num.append(i)
    print(prime_num)


n = 122
print_prime(n)
        