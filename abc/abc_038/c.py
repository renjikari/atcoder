import sys

def main():
    n = int(input())
    a = list(map(int,input().split()))

    con = 0
    ans=0

    for i in range(1,n):
        con +=1
        if not a[i-1] < a[i]:
            ans += wa(con)
            con =0

    con+=1
    ans += wa(con)

    print(ans)


def wa(num):
    re=0
    for i in range(1,num+1):
        re+=i
        
    return re

if __name__ == "__main__":
        main()
