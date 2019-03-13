import sys

def main():
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))


    Flag = False
    biga = 0
    lessa = 0
    for i in range(n):
        if a[i] > b[i]:
            biga += a[i] - b[i]
        else:
            lessa += (b[i] - a[i]) //2

    tmp = lessa - biga

    if tmp >= 0:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
