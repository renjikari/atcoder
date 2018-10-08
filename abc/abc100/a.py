import sys

def main():
    a,b = input().split()
    a = int(a)
    b = int(b)

        
    if a > 8 or b > 8:
        print(":(")
    else:
        print("Yay!")

if __name__ == "__main__":
        main()
