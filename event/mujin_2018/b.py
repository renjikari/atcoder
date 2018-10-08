import sys

def main():
    a = int(input())
    s = input()

    for i in s:
        if a == 0:
            print("Yes")
            exit()
        if i == "+":
            a += 1
        else:
            a -= 1

    if a == 0:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
        main()
