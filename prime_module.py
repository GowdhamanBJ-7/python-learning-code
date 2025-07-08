def is_prime(n):
    if n < 2:
        return 'Give number greater than 2'
    for i in range(2, n):
        if n % i == 0:
            return 'Not a prime'
    return 'Prime'

def add(a,b):
    return a + b
