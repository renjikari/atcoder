import sys

def main():
    n = input()

    if len(n) == 2:
        print(n)
    else:
        print(n[::-1])
       

if __name__ == "__main__":
        main()
