import sys

def main():
    n, x = map(int,input().split())
    x  = list(map(int,input().split()))

    ans = 0
    for i in range(50):
        tmp = 0

        if tmp > 100*i or i == n:
            for j,k in enumerate(range(1,i)[::-1]):
                ans += x[j]*(k*2+1) + 100
            ans += 100 if i !=0 else 0
            x =  x[i:]

        for j,k in enumerate(range(2,2*(i+2),2)[::-1]):
            tmp += x[j] * k

    print(ans)

   
if __name__ == "__main__":
        main()
