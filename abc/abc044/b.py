import sys

def main():
    w = list(input())

    for i in w:
        if w.count(i)%2 != 0:
            print("No")
            exit()

    print("Yes")

    

if __name__ == "__main__":
        main()
