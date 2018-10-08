import math
from operator import mul
from functools import reduce

def main():
    n = int(input())
    a = list(map(int,input().split()))

    """
    gcd = a[0]
    lcm =0
    for i in range(1,len(a)):
        gcd = math.gcd(gcd,a[i])
        lcm = reduce(mul,a[:i+1])//gcd 
        print(gcd)
        #print(lcm)
        #print(a[i])
    """
    ans= 0
    for i in a:
        ans += (i-1)

    print(ans)


if __name__ == "__main__":
        main()
