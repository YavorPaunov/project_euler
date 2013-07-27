import sys
sys.path.append('../')

from utils import is_prime;

def nth_prime(n):

    found = 0;
    i = 1;
    
    while found < n:
        i += 1;
        if is_prime(i):
             found += 1;

    return i;

if __name__ == "__main__":
    print(nth_prime(10001));