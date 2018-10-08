import sys

def main():
    n = int(input())
    k = int(input())


    ans = 1
    for i in range(n):
        if ans < k:
            ans += ans
        else:
            ans += k

    print(ans)


if __name__ == "__main__":
        main()
