import sys

def main():
    a, b, x = map(int,input().split())

    ans=(b - a+1)//x
    amari = (b-a+1)%x

    if amari ==0:
        print(ans)
        exit()
    if a%x ==0:
        ans+=1
    elif amari > x- (a%x):
        ans+=1
    
    print(ans)


if __name__ == "__main__":
        main()
