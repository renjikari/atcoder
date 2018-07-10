def main():
    n, a, b= input().split()
    n = int(n)
    a = int(a)
    b = int(b)
    
    lst = []
    for i in range(a, b+1):
        for n in range(1,n+1):
            if (n//10000 + n%10000//1000 + n%1000//100 + n%100//10 + n%10) == i:
                lst.append(n)

#    print(lst)

    ans = 0
    for i in lst:
        ans += i

    print(ans)

if __name__ == "__main__":
        main()
