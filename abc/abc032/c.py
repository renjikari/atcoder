import sys

def main():
    n,k = map(int,input().split())
    lst =[]
    for i in range(n):
        lst.append(int(input()))

    seki = 1
    ans=0
    anslst=[0]

    if 0 in lst:
        print(n)
        exit()

    for i in range(n-1):
        if n-max(anslst) < i:
            break

        for j in lst[i:]:
            seki *= j
            if seki > k:
                anslst.append(ans)
                ans = 0
                seki = 1
                break

            if lst[::-1].index(j) == 0:
                anslst.append(len(lst[i:]))
                ans = 0
                seki = 1
                break
            ans+=1
    
    print(anslst)
    print(max(anslst))


if __name__ == "__main__":
        main()
