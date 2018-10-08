import sys

def main():
    n = int(input())
    a1 = list(map(int,input().split()))
    a2 = list(map(int,input().split()))

    anslst = []
    for i in range(n):
        ans = 0
        for j in range(n):
            if i > j:
                ans += a1[j]
            elif i == j:
                ans +=  a1[j] + a2[j]
            elif i < j:
                ans += a2[j]
        anslst.append(ans)

    print(max(anslst))
                
       

if __name__ == "__main__":
        main()
