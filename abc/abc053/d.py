import sys

def main():
    n = input()
    a = input().split()
    n = int(n)
    a = list(map(int, a))
        

    lst = [0]* 1000000
    dup = 0
    ans =0

    for i in a:
        lst[i]+=1

    for i in lst:
        if i >0:
            ans+= 1
        if i > 1:
            dup = dup + i - 1

    if dup % 2 == 0:
        print(ans)
    else:
        print(ans-1)

if __name__ == "__main__":
        main()
