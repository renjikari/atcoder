import sys
import math

def main():
    n = int(input())

    lst = [0 for i in range(n)]
    for i in range(n):
        lst[i] = int(input())


    lst = sorted(lst)[::-1]

    ans = 0
    for i in range(n):
        if i %2 == 0:
            ans += lst[i] **2 * math.pi 
        else:
            ans -= lst[i] **2 * math.pi 

    print(ans)


if __name__ == "__main__":
        main()
