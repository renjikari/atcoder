import sys
import math

def main():
    a, b, c = map(int,input().split())

    def ft(t,a,b,c):
        return (a*t) + (b*math.sin(c*t*math.pi))

    goal = 100
    low = 0.0000001
    high = 200
    t = (low + high)/2

    while low <=high:
        if goal-0.0000001 <= ft(t,a,b,c) <= goal+0.0000001:
            print(t)
            exit()

        elif goal > ft(t,a,b,c):
            low = t
        else:
            high = t

        t = (low+high)/2

    

if __name__ == "__main__":
        main()
