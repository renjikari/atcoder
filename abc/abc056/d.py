import sys

def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    
    a = sorted(a)
    re = a[::-1]
    
    ans = n
    for i in range(n):
        wa = 0
        for j in range(i,n):
            wa += re[j]
            if wa >= k:
                ans = n - j -1
                break

        if wa < k:
            #print(ans)
            break

    for i in a[:ans]:
        tmp = a.count(i)
        if tmp > 1:
            ans+= (tmp-1)

    print(ans)



    

if __name__ == "__main__":
        main()
