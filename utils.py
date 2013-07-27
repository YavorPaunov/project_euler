from math import sqrt;

def is_prime(n):  
    if n <= 1: return False;
    if n == 2: return True;
    if n % 2 == 0: return False;
    
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False;
    return True;
    
def esieve(lim):
    primes = [j for j in range(2, lim+1)];
    m = int(sqrt(lim))+1;
    for i in range(2, m):
        for n in range(i*2, lim+1, i):
            if n in primes:
                primes.remove(n);
    return primes;

if __name__ == "__main__":
    print(esieve(1000));