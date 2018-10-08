import sys

def main():
    N = input()
    a = input().split()

    a = list(map(int,a))
        
    ans = 0

    for i in a:
        while True:
            if i%2==0:
#                print(i)
                i = i/2
                ans+=1
                continue
            else:
                break

    print(ans)


if __name__ == "__main__":
        main()
