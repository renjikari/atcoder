import sys

def calc(n,act, lst):
    low = 0
    high = n -1
    while low <= high:
        mid = (low + high) //2
        guess = lst[mid]
        if guess > act:
            high = mid
            continue
        if guess < act:
            low = mid
            continue
        if guess == act:
                return n-mid,lst[mid+1]

        if a[i] < b[j]:
            for k in range(n):
                if b[j] < c[k]:
                    ans+=1
                else:
                    break
        else:
            break


def main():
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    c = list(map(int,input().split()))

    a= sorted(a)[::-1]
    b= sorted(b)[::-1]
    c= sorted(c)[::-1]
        
    ans=0



    for i in range(n):
        B_ans,B = calc(n,a[i], b)
        C_ans,C = calc(n, B, c)
        ans += B_ans * C_ans


    print(ans)

if __name__ == "__main__":
        main()
