import sys

def main():
    n = int(input())
    F = [0 for i in range(n)]
    P = [0 for i in range(n)]


    for i in range(n):
        F[i] = list(map(int,input().split()))

    for i in range(n):
        P[i] = list(map(int,input().split()))

    ans = 0
    Flag = "first"

    for z in range(1,1024):
        ans_list = list(map(int,list(format(z,"010b"))))
        pro = 0

        for i in range(n):
            tmp = 0
            for j in range(10):
                if ans_list[j] == 1 and F[i][j]== 1:
                    tmp += 1

            pro += P[i][tmp]

        if Flag == "first":
            ans = pro
            Flag = False

        ans = max(ans, pro)


    print(ans)


if __name__ == "__main__":
        main()
