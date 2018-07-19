import sys

def main():
    n = int(input())
    a = list(map(int,input().split()))
    onaji =[]
    tmp = 0
    now = 0

    for i in range(n):

        if now == a[i]:
            tmp+=1
        else:
            onaji.append(tmp)
            tmp = 1
            now = a[i]

    onaji.append(tmp)

    ans = 0
    for i in onaji:
        ans += i//2
        

    print(ans)

        


    
if __name__ == "__main__":
        main()
