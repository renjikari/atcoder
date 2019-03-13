import sys

def main():
    n, m = map(int,input().split())
    lst=[]

    for i in range(m):
        lst.append(list(map(int,input().split())))

    nozoku = 0
    grant = 0

    for i in range(n-1):
        nozoku = i + 0.5
        for j in range(m)
            if lst[j][0] < i < lst[j][1] :
            grant +=1


if __name__ == "__main__":
        main()
