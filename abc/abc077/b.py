import sys

def main():
    n = int(input())

    ans = 1
    for i in range(1,n):
        if i*i > n:
            break
        ans = i*i

    print(ans)


if __name__ == "__main__":
        main()
