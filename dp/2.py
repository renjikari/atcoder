N,W=input().split()
N=int(N)
W=int(W)

weight = []
value = []

for i in range(N):
    w,v = input().split()
    weight.append(int(w))
    value.append(int(v))

dp = [[0]*(W)]*(N+1)

for n in range(N):
    for w in range(W):
        if w >= weight[n]:
            dp[n+1][w] = max(dp[n][w-weight[n]] + value[n], dp[n][w])
        else:
            dp[n+1][w] = dp[n][w]

#print(weight)
#print(value)
#print(dp[n][w])
print(dp)


