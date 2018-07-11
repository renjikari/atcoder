import sys
import numpy as np

def main():
    n,a,b = map(int,input().split())
    sd = []

    for i in range(n):
        s,d = input().split()
        d = int(d)
        sd.append([s,d])


    ans = 0
    for i in range(n):
        if sd[i][0] == "East":
            if sd[i][1] < a:
                ans += a
            elif b < sd[i][1]:
                ans += b
            else:
                ans += sd[i][1]
        elif sd[i][0] == "West":
            if sd[i][1] < a:
                ans -= a
            elif b < sd[i][1]:
                ans -= b
            else:
                ans -= sd[i][1]

    if ans == 0:
        print(0)
    if ans < 0:
        print("West " + str(abs(ans)))
    if ans > 0:
        print("East " + str(abs(ans)))

if __name__ == "__main__":
        main()
