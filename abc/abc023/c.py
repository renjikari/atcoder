import sys
import numpy as np

def main():
    R, C, K = map(int,input().split())
    n = int(input())
    #arr = np.array([[0 for i in range(C)]for i in range(R)])
    ans = np.array([[0 for i in range(C)]for i in range(R)])

    r = [0 for i in range(R)]
    c = [0 for i in range(C)]

    for i in range(n):
        rtmp, ctmp = map(int,input().split())
        #arr[r-1][c-1] = 1
        r[rtmp-1]+=1
        ans[rtmp-1]+=1
        ans.transpose()[ctmp-1]+=1

        ans[rtmp-1][ctmp-1] -= 1
        

    """
    for i in range(R):
        ans[i] += r[i]
        
    for i in range(C):
        ans.transpose()[i] += c[i]
    """

    print(np.sum(ans==K))


    """
    for i in range(R):
        for j in range(C):
            candy = np.sum(arr[i] == 1) + np.sum(arr.transpose()[j] == 1)
            if arr[i][j] == 1:
                candy -= 1

            if candy == K:
                ans +=1
    """

    """
    f = max(R,C)

    for i in range(f):
        if i < R:
            can = np.sum(arr[i] == 1)
            ans[i] += can

        if i < C:
            can = np.sum(arr.transpose()[i]==1)
            ans.transpose()[i] += can

    print(np.sum(ans==K))
    """


if __name__ == "__main__":
        main()
