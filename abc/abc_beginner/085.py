import sys

def main():
    N = int(input())
    lst = []
    for i in range(N):
        lst.append(int(input()))
        

    lst = set(lst)
    print(len(lst))


if __name__ == "__main__":
        main()
