import sys

def main():
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))


    Flag = False
    biga = 0
    lessa = 0
    for i in range(3):
        if a[i] > b[i]:
            biga += a[i] - b[i]
        else:
            lessa1 += b[i] - a[i]

    tmp = lessa -(biga*2)

    if tmp <0:
        print("No")
    elif tmp ==0:


    else:
        print("Yes")

if __name__ == "__main__":
    main()
