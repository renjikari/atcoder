import sys

def main():
    s = input()
    n = int(input())

    ans = ""
    if n % 5==0:
        print(s[n//5 -1]+s[4])
    else:
        print(s[n//5] + s[n%5-1] )

if __name__ == "__main__":
        main()
