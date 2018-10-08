import sys

def main():
    n, l = map(int,input().split())
    s =[]
    for i in range(n):
        s.append(input())


    print("".join(sorted(s)))

if __name__ == "__main__":
        main()
