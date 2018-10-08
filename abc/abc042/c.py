import sys

def main():
    n, k = map(int,input().split())
    d = list(input().split())


    ans = n

    Flag = False
    while True:
        for i in range(k):
            if list(str(ans)).count(d[i]) > 0:
                ans+=1
                Flag = True
                break
            if i == k -1:
                print(ans)
                exit()


if __name__ == "__main__":
        main()
