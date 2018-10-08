import sys

def main():
    n, x = map(int,input().split())
    a = list(map(int,input().split()))

    a = sorted(a)
    ans = 0
    tmp = 0
    for i in a:
        tmp += i
        if tmp <= x:
            ans+=1

    if n == ans:
        if sum(a) != x:
            ans-=1

    print(ans)


       

if __name__ == "__main__":
        main()
