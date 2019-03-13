import sys

def main():
    n = int(input())
    a = list(map(int,input().split()))

    ans = 0
    for i in a:
        if i % 2==0:
            while True:
                ans+=1
                i = i//2
                if i%2==0:
                    continue
                else:
                    break

    print(ans)
       

if __name__ == "__main__":
        main()
