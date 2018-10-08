def main():
    a, b, c = input().split()
    k = input()

    a = int(a)
    b = int(b)
    c = int(c)
    lst = [a,b,c]
    k = int(k)


    M = max(lst)
    lst.remove(M)

    for i in range(k):
        M = M * 2
    ans = sum(lst) + M

    print(ans)
        
if __name__ == "__main__":
        main()
