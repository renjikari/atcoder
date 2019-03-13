import sys
import time

n, k = map(int,input().split())

ans = 0

if k == 0:
    print(n *n)
    exit()

#start = time.time()
"""
for a in range(k, n+1):
    ans += (n - a)
    for b in range(k,a-k+1):
        if a % b >= k:
            ans += 1
"""

for b in range(k+1, n+1):
    ans += (b-k)
    ans += (n-k)//b

#elapsed_time = time.time() - start

print(ans)
#print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")

