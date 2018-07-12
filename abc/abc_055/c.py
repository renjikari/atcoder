import sys

def main():
    n, m = map(int,input().split())
    ans=0

    if m < n*2:
        ans = m//2
    elif m >= n *2:
        ans += n
        m -= n*2
        ans += m//4

    print(ans)

if __name__ == "__main__":
        main()
