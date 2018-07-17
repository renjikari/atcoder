import sys

def main():
    n = int(input())
    lst=[]

    for i in range(n):
        lst.append(int(input()))

    now = 1
    ans = 0
    for i in range(n):
        now = lst[now-1] 
        ans +=1
        if now == 2:
            print(ans)
            exit()

    print(-1)

if __name__ == "__main__":
        main()
