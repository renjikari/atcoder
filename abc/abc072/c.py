import sys

def main():
    n = int(input())
    a = list(map(int,input().split()))

    #lst = [0 for i in range(n*3)]
    ans_lst = [0 for i in range(max(a)+4)]
    """
    for i in range(n):
        lst[3*i] = a[i]
        lst[3*i+1] = a[i]+1
        lst[3*i+2] = a[i]+2
    """

    for i in a:
        ans_lst[i] += 1
        ans_lst[i+1] += 1
        ans_lst[i-1] += 1

    """
    ans = -1
    for i in set(lst):
        ans = max(lst.count(i),ans)
    """

    print(max(ans_lst))


if __name__ == "__main__":
        main()
