import sys

def main():
    a = int(input())
    b = int(input())
    n = int(input())

    flag=0

    while flag==0: 
        if n%a == 0 and n%b ==0:
            print(n)
            exit()
        n += 1


if __name__ == "__main__":
        main()
