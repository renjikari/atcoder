import sys

def main():
    n, t = map(int,input().split())
    lst = list(map(int,input().split()))


    m = 0
    M = N +1
    tmp = lst[0]
    ans = 0

    for i in lst:
        if i < m:
            m = i

        if i > M:
            M = i

        ans += 1
        




if __name__ == "__main__":
        main()
