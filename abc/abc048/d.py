import sys

def main():
    s = list(input())

    if s[0] == s[-1]:
        if len(s) %2 ==0:
            print("First")
        else:
            print("Second")
    else:
        if len(s) % 2==0:
            print("Second")
        else:
            print("First")



if __name__ == "__main__":
        main()
