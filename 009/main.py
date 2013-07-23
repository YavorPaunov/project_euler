# author: Yavor Paunov

def pyt_triplets(sum):
    for a in range(1, sum):
        for b in range(a+1, sum):
            c = sum - a - b;
            if a*a + b*b == c*c:
                return a * b * c;
    
if __name__ == "__main__":
    print(pyt_triplets(1000));