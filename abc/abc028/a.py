import sys

def main():
    n = int(input())

    if n == 100:
        print("Perfect")
    elif n >= 90:
        print("Great")
    elif n>=60:
        print("Good")
    else:
        print("Bad")

if __name__ == "__main__":
        main()
