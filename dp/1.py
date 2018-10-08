
n=input()
n=int(n)

a = input().split()
a = [int(i) for i in a]

dp = [0]

for i in range(n):
    dp.append(max(dp[i], dp[i]+a[i]))

print(dp[n])


