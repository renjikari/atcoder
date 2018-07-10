def main():
    a = int(input()) #500円玉
    b = int(input()) #100円玉
    c = int(input()) #50円玉
    x = int(input()) #合計

    lst = []
    ans = 0

    for a in range(0,int(a)+1):
        for b in range(0,int(b)+1):
            for c in range(0,int(c)+1):
                lst.append(500*a + 100*b + 50*c)

    for i in lst:
        if i == x:
            ans += 1

    print(ans)

if __name__ == "__main__":
        main()
