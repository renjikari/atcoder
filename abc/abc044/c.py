import sys

def main():
    n, a = map(int,input().split())
    x = list(input())
        
    ans =0
    mid =[][]

    for i in range(n):
        mid.append([x[i]])

    for i in range(n):
        for j in range(n):
            mid[i].append(mid[i][j] + x[j])



if __name__ == "__main__":
        main()
