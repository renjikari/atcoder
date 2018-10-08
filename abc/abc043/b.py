import sys

def main():
    s = list(input())

    while "B" in s:
        b = s.index("B")
        if b != 0:
            s.pop(b-1)
            s.pop(b-1)
        else:
            s.pop(b)

    print("".join(s))
    

if __name__ == "__main__":
        main()
