import sys

def main():
    a, b, c,d = input().split()
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)

    if a*b < c*d:
        print(c*d)
    else:
        print(a*b)

if __name__ == "__main__":
        main()
