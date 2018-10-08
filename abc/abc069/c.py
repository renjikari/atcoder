import sys

def main():
    n = int(input())
    a = list(map(int,input().split()))
    
    four = 0
    two = 0

    for i in a:
        if i %4 ==0:
            four +=1
        elif i %2==0:
            two +=1


    if two > 0:
        if (n-two)/2 <= four:
            print("Yes")
        else:
            print("No")
    else:
        if n//2 <= four:
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
        main()
