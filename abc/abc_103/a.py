import sys

def main():
    a,b,c = map(int,input().split())

    lst = []
    # aから
    lst.append(abs(b-a) + abs(c-b))
    lst.append(abs(c-a) + abs(b-c))

    # bから
    lst.append(abs(a-b) + abs(c-a))
    lst.append(abs(c-b) + abs(a-c))

    # cから
    lst.append(abs(c-b) + abs(a-c))
    lst.append(abs(a-c) + abs(b-a))

    print(min(lst))

if __name__ == "__main__":
        main()
