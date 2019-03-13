import sys
import numpy as np

def main():
    n, m = map(int,input().split())
    lst = []
    for i in range(n):
        lst.append(list(input()))

    minus = (n*m)-n-m +1
    ans = ((n*m)-n-m+1) * n*m
    print("start: " + str(ans))

    lst = np.array(lst)
    tenchi = np.array(lst).transpose()

    allsharp = np.sum(lst == "#")
    
    for i in range(n):
        for j in range(m):
            if lst[i][j] != "#":
                continue

            ans -= minus

            tmp  = np.sum(lst[i] == ".")
            tmp2 = np.sum(tenchi[j] == ".")

            ans -= tmp * tmp2

            sharp = minus - (allsharp - 1 - (n+m -2 -tmp -tmp2))
            ans -= sharp
            
            print(ans)

    print(ans)
            

if __name__ == "__main__":
        main()
