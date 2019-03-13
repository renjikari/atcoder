import sys

def main():
    t = int(input())
    A=[]
    B=[]
    C=[]
    D=[]

    for i in range(t):
        a,b,c,d = map(int,input().split())
        A.append(a)
        B.append(b)
        C.append(c)
        D.append(d)

    for i in range(t):
        ans = "Yes"

        if A[i] < B[i] or B[i] > D[i]:
            print("No")
            continue

        if B[i]-1 <= C[i]:
            print("Yes")
            continue

        lst = []

        tmp = (A[i] + D[i]) % B[i]
        f = tmp
        if tmp > C[i]:
                print("No")
                continue

        lst.append(tmp)

        for j in range(1,B[i]):
            tmp = (tmp + D[i]) % B[i]

            tmp2 = (D[i] % B[i]) * B[i]

            if tmp > C[i]:
                ans = "No"
                break

            if tmp in lst:
                break

            lst.append(tmp)

        for j in range(C[i],B[i]):
            n = (j - (A[i]%B[i]))/(D[i]%B[i])
            if isinstance(n, int):
                print("No")
                continue

        print(ans)


if __name__ == "__main__":
        main()
