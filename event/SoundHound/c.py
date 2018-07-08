import sys
import numpy as np

def main():
    n,m,d = input().split()
    n = int(n)
    m = int(m)
    d = int(d)
        

    #美しくなる組み合わせ
    if d ==0:
        c = n # d =0

        # all = c * ((n-1)**(m-2)) * (m-2)
        #                ↑possible
        p = (n/((n-1)**2)) * (((n-1)/n)** m) * (m-1)

    if d > 0:
        c = (n-d) * 2 # d > 0
        # possibleをもとめる
        possible = ( ((n-1) * ((d*2)/n)) + ((n-2) * ((n-(d*2))/n)) ) ** (m-2)

        a = c * possible * (m-1)
        p = a/(n**m)

    print(p)

if __name__ == "__main__":
        main()
