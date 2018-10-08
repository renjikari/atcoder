import sys

def main():
    a, b = input().split()
    a = int(a)
    b = int(b)

    if a > b:
        print(a-1)
    else:
        print(a)
        
if __name__ == "__main__":
        main()
