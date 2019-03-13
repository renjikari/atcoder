n,k = map(int,input().split())

ans = 0

ans += (k-1)*(n-k) *6

ans += (n-1)*3

ans+= 1

print(ans/n/n/n)
