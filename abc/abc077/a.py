import sys

def main():
    a = input()
    b = input()


    if a[::-1] == b:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
        main()
