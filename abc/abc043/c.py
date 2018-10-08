import sys
from statistics  import mean

def main():
    n = int(input())
    a = list(map(int,input().split()))

    ave = mean(a)
    ave = round(ave)

    ans =0
    for i in a:
        ans += (i-ave)**2

    print(ans)
    

if __name__ == "__main__":
        main()
