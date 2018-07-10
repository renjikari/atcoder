import sys

def main():
    a, b = input().split()
    a = int(a)
    b = int(b)

    ans = a*b
    if ans % 2 is 0:
        print("Even")
    else:
        print("Odd")

if __name__ == "__main__":
        main()
