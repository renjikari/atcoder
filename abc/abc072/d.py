import sys

def main():
    n = int(input())
    p = list(map(int,input().split()))


    ans =0
    Flag = False

    for i in range(n-1):
        if Flag== True:
            Flag = False
            continue

        if p[i] == i+1:
            ans+=1
            if p[i+1] == i+2:
                Flag = True

    if Flag == False:
        if p[-1] == n:
            ans+=1

    print(ans)

if __name__ == "__main__":
        main()
