import sys

def main():
    n, k = map(int,input().split())
    lst = list(map(int,input().split()))

    n = n -k + 1

    ans = sum(lst)*min(n,k)
    #ans = sum(lst)*k
    j = 0

    #re = lst[::-1]
    for i in range(min(n,k))[::-1]:
        ans -= (lst[j] * i) + (lst[-j-1] * i)
        j += 1
        
    print(ans)



if __name__ == "__main__":
        main()
