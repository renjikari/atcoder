import sys

def main():
    n, k = map(int,input().split())

    ans = 0

    ans +=1
    ans += (n-1)*3
    ans += (k-1)*(n-k)*6

    print(ans/n/n/n)

if __name__ == "__main__":
        main()
