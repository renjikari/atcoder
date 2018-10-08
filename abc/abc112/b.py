import sys

def main():
    n, t = map(int,input().split())

    lst = [0 for i in range(n)]
    for i in range(n):
        lst[i] = list(map(int,input().split()))

    ans = 10000
    for i in lst:
        if i[1] <= t:
            ans = min(ans,i[0])

    if ans > 9999:
        print("TLE")
    else:
        print(ans)
       

if __name__ == "__main__":
        main()
