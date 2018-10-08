import sys

def main():
    n, x = map(int,input().split())
    a = list(map(int,input().split()))

    ans=0

    if a[0] > x:
        tmp = a[0] -x
        a[0] -= tmp
        ans+=tmp 

    for i in range(n-1):
        if a[i] + a[i+1] > x:
            tmp = (a[i]+a[i+1]) -x
            a[i+1] -= tmp
            ans += tmp

    print(ans)

if __name__ == "__main__":
        main()
