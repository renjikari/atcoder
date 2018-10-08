import sys

def main():
    a, b = input().split()
    a = int(a)
    b = int(b)

    if a < b:
        print("Better")
    else:
        print("Worse")

if __name__ == "__main__":
        main()
