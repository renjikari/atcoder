import sys
import itertools

def main():
    n, k = map(int,input().split())

    if k %2 ==0:
        tmp = n//k
        ans = 0
        for i in range(1,n+1):
            if (i +i) %k == 0:
                ans+=1
                for j in range(1, n+1):
                    if (i+j) %k == 0 and i!=j:
                        ans += 3
        #ans = tmp+1
        #ans += (tmp+1)*(tmp)*3
        ans += tmp * (tmp-1) * (tmp-2)
        print(int(ans))
 
    else:
        tmp = n//k 
        ans = tmp
        ans += tmp * (tmp-1)*3
        ans += tmp * (tmp-1) * (tmp-2)
        print(int(ans))
      


if __name__ == "__main__":
        main()
