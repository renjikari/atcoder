import sys

def main():
    n = int(input())
    ans = 1

    for i in range(1,n+1):
        ans *= i
        if ans >= 1000000007:
            ans = ans %1000000007

    print(ans)

if __name__ == "__main__":
        main()
