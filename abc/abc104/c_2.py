import sys
import numpy as np

def main():
    D, G = map(int, input().split())

    p = [0] * D
    G = [0] * D

    for i in range(D):
        p[i], G[i] = map(int,input().split())


    print(p)
        
    

def func(N, M, lst):
    al = []
    #print(lst)
    lst1 = list(map(int, lst))
    lst2 = list(map(int, lst))
    #print(lst)

    for i in range(len(lst1)): 
        for j in range(len(lst2)):
            if not i == j:
                al.append(lst1[i] + lst2[j])
    ans = 0
    for a in al:
        if a > ans and a <= M:
            ans = a;

    if ans == 0:
        ans = "NONE"
    return ans


if __name__ == "__main__":
        main()
