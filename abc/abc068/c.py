import sys

def main():
    n, m = map(int,input().split())
    lst = [0 for i in range(n)]
    for i in range(m):
        lst[i] = list(map(int, input().split()))

    lst2 = []
    for i in range(m):
        if i[1] == n:
            lst2.append(i)
        
    for i in lst2:
        if i




    for i in range(n):
        lst[i] = int(input())
       

if __name__ == "__main__":
        main()
