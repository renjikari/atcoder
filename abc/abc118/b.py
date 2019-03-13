import sys

def main():
    n, m = map(int,input().split())

    lst = [0 for i in range(n)]
    for i in range(n):
        lst[i] = list(map(int,input().split()))[1:]


    tmp = [i for i in range(1,m+1)]
    for i in lst:
        tmp = set(tmp) & set(i)

    print(len(tmp))
       

if __name__ == "__main__":
        main()
