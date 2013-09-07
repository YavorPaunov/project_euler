from math import sqrt;

# Check if number is prime
def is_prime(n):  
    if n <= 1: return False;
    if n == 2: return True;
    if n % 2 == 0: return False;
    
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False;
    return True;
    
# Generate prime numbers up to a given limit 
def esieve(lim):
    primes = [j for j in range(2, lim+1)];
    m = int(sqrt(lim))+1;
    for i in range(2, m):
        for n in range(i*2, lim+1, i):
            if n in primes:
                primes.remove(n);
    return primes;

# Find greated common divider of two numbers
# Euclid's algorithm
def gcd(a, b):
    if b == 0: return a;
    return gcd(b, a%b);

# Find lowest common multiplier
def lcm(a, b):
    return a*b/gcd(a,b);
      
# Heap sort:
def hsort(arr):
    __buildHeap(arr);s
    for i in range(len(arr)-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0];
        __heapify(arr, 0, i);
        
def __buildHeap(arr):
    for i in range(int(len(arr) / 2)-1, -1, -1):
        __heapify(arr, i, len(arr));

def __heapify(arr, idx, max):
    left = 2 * idx + 1;
    right = 2 * idx + 2;
    
    largest = idx;
    if left < max and arr[left] > arr[largest]:
        largest = left;
    
    if right < max and arr[right] > arr[largest]:
        largest = right;
    
    if largest != idx:
        arr[idx], arr[largest] = arr[largest], arr[idx];
        heapify(arr, largest, max);

# Insertion sort:
def isort(ar):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j];
                

# Quicksort:
def qsort(arr):
    if len(arr) > 1:
        pivot = arr[0];
        less = [i for i in arr if pivot > i];
        greater = [i for i in arr if pivot < i];
        eq = [i for i in arr if pivot == i];
        return qsort(less) + eq + qsort(greater);
    return arr;
    
# Merge-sort
def msort(arr):
    if len(arr) == 1:
        return arr;
        
    middle = int(len(arr) / 2);
    
    left = msort(arr[0:middle]);
    right = msort(arr[middle:]);
    result = [];
    
    while len(left) > 0 and len(right) > 0:
        if left[0] < right[0]:
            result.append(left.pop(0));
        elif left[0] > right[0]:
            result.append(right.pop(0));
        else:
            result.append(left.pop(0));
            result.append(right.pop(0));
    result += left + right;
    
    return result;


class RedBlack:
    def __init__(self, root):
        self.root = root
        
    def __validate(self, node):
        
        
    class Node:
        def __init__(self, data):
            self.red = false
            self.data = data
            self.left = None
            self.right = None
        
        
# For testing:
if __name__ == "__main__":
    from random import random;  
    arr = [int(100 * random()) for i in range(30)];
    print(arr);
    a = msort(arr);
    print(a);
    
