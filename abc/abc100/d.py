import sys

def main():
    N, M = input().split()
    lst = []

    N = int(N)
    M = int(M)
    for i in range(N):
        a = input().split()
        lst.append(a)

    print(N)
    print(M)
    print(lst)
    dp = [0]*M
    sum = [0]*3

    #総和をjとする
    dp = [[0 for i in range(M+1)]for j in range(N+1)]

    dp[0][0] =[0,0,0]
    dp[0][1] =lst[0] #[1,2,3]
    dp[0][2] =lst[0] #[1,2,3]
    dp[0][3] =lst[0] #[1,2,3]
    dp[0][4] =lst[0] #[1,2,3]

    for i in range(N):
        for j in range(M)
            if 
                dp[i+1][j]=dp[i][j-1]+lst[i]

                dp[i+1][j]=dp[i][j]

                dp[i+1][j] = dp[i-1][j]



    """
    if N == 0 and M == 0:
        sys.exit()
    lst = input().split()
    ans = func(N, M, lst)
    print(ans)
    """

def func(N, M, lst):
    al = []
    #print(lst)
    lst1 = list(map(int, lst))
    lst2 = list(map(int, lst))
    #print(lst)

    for i in range(len(lst1)): 
        for j in range(len(lst2)):
            if not i == j:
                al.append(lst1[i] + lst2[j])
    ans = 0
    for a in al:
        if a > ans and a <= M:
            ans = a;

    if ans == 0:
        ans = "NONE"
    return ans


if __name__ == "__main__":
        main()
