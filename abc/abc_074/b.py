import sys

def main():
    N = int(input())
    K = int(input())
    x = list(map(int,input().split()))
    ans = 0    

    for i in x:
        ans+= min(i , abs(K -i)) *2

    print(ans)

if __name__ == "__main__":
        main()
