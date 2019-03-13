import sys

def main():
    n = int(input())
    a, b = map(int,input().split())

    lst = [0 for i in range(n)]
    for i in range(n):
        lst[i] = int(input())

if __name__ == "__main__":
        main()
