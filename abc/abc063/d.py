import sys
import numpy as np

def main():
    n, a, b = map(int,input().split())

    h = np.zeros(n)
    for i in range(n):
        h[i] = int(input())

    h = h.sort()[::-1]




    #tmp = a-b
    #ans = 0
    #while (h<=0).all() == False:
    #    h = h - b
    #    h[np.argmax(h)] -= tmp
    #    ans+=1



    print(ans)

    

if __name__ == "__main__":
        main()
