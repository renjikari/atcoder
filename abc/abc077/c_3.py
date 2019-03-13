import sys

def calc(n,act,lst):
    if lst[-1] < act:
        return n
    if lst[0] > act:
        return 0
    if lst[-1] == act:
        return n-1

    low = 0
    high = n-1
    mid = (low + high)//2
    tmp = -1
    while True:
        if lst[mid] == act:
            return mid
        elif lst[mid] < act:
            low = mid
            mid = (low + high)//2
            if tmp == mid:
                return mid+1
            else:
                tmp = mid

        elif lst[mid] > act:
            high = mid
            mid = (low + high)//2


def calc2(n,act,lst):
    if lst[-1] < act:
        return n
    if lst[0] > act:
        return 0
    if lst[-1] == act:
        return n


    low = 0
    high = n-1
    #切り上げのため+1してる
    mid = (low + high+1)//2
    tmp = -1
    while True:
        if lst[mid] == act:
            return mid+1
        elif lst[mid] < act:
            low = mid
            mid = (low + high+1)//2
            if tmp == mid:
                return mid
            else:
                tmp = mid

        elif lst[mid] > act:
            high = mid
            mid = (low + high+1)//2
            if tmp == mid:
                return mid
            else:
                tmp = mid



def main():
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    c = list(map(int,input().split()))

    a= sorted(a)
    b= sorted(b)
    c= sorted(c)

    ans = 0
    for i in range(n):
        aans = calc(n,b[i],a)
        cans = calc2(n,b[i],c)
        #print(aans)
        #print(cans)
        ans += aans * (n-cans)

    """
    for i in range(n):
        tmp = calc(n,c[i],b)
        ans += sum(blist[:tmp])
    """

    print(ans)


if __name__ == "__main__":
        main()
