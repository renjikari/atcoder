import sys

def main():
    s = list(input())
    t = list(input())


    for i in range(len(t)):
        if t == s:
            print("Yes")
            exit()
        t.insert(0,t.pop())

    print("No")

if __name__ == "__main__":
        main()
