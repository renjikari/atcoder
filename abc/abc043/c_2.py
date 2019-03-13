n = int(input())
a = list(map(int, input().split()))

ave = round(sum(a)/n)

ans = 0
for i in a:
    ans += (ave - i)**2

print(ans)
