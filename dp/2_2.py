
n, W = input().split()
n = int(n)
W= int(W)

weight=[]
value=[]


for i in range(n):
    w ,t = map(int,input().split())
    weight.append(w)
    value.append(t)


# dp[i+1][w] = dp[i][w] 
# dp[i+1][w] = dp[i][w - weight[i]] + value[i]

dp = [[0]*W]*(n+1)
#dp = [[0]]*(n+1)

for w in range(W):
    dp[0][w] = 0

for i in range(n):
    for w in range(W):
        if w < weight[i]:
            dp[i+1][w] = dp[i][w]
        else:
            dp[i+1][w] = dp[i][w - weight[i]] + value[i]

print(dp)
    



