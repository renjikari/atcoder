import sys
import math

def main():
    n,m = map(int,input().split())

    if abs(n-m) > 1:
        print(0)

    elif n == m:
        ans = math.factorial(n) * math.factorial(m) * 2
        print(ans%1000000007)

    else:
        ans = math.factorial(n) * math.factorial(m)
        print(ans%1000000007)



if __name__ == "__main__":
        main()
