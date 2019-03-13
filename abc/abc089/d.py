import sys

def main():
    H,W,D  = map(int,input().split())

    #lst = [0 for i in range(n)]
    lst = [[0 for i in range(W)] for j in range(H)]
    for i in range(H):
        lst[i] = list(map(int,input().split()))

    lst = [ y for x in lst for y in x]
    Q = int(input())

    lr=[0 for i in range(Q)]
    for i in range(Q):
        lr[i] = list(map(int,input().split()))


    for i in range(Q):
        start = lr[i][0]
        goal = lr[i][1]
        n = (goal - start)//D
        ans = 0
        for j in range(n):
            h1 = lst.index(start)//W
            w1 = lst.index(start) - (h1*W)
            h2 = lst.index(start+D)//W
            w2 = lst.index(start+D) - (h2*W)
            #print(abs(h2-h1)+abs(w2-w1))
            ans += abs(h2-h1)+abs(w2-w1)
            start = start+D

        print(ans)



if __name__ == "__main__":
        main()
