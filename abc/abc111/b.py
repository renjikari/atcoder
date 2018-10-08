import sys

def main():
    n = int(input())

    if n > int(str(n//100)*3):
        print(int(str(n//100+1)*3))
    else:
        print(int(str(n//100)*3))

      

if __name__ == "__main__":
        main()
