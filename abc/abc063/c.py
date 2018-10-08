import sys

def main():
    n = int(input())
    s = [0]*n
    for i in range(n):
        s[i] = int(input())

    ans = sum(s)
    if ans % 10 != 0:
        print(ans)
        exit()

    s = sorted(s)

    for i in s:
        if i % 10 == 0:
            continue
        else:
            print(ans -i)
            exit()

    print(0)

        

if __name__ == "__main__":
        main()
