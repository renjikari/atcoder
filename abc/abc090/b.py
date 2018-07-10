import sys

def main():
    a,b = map(int,input().split())
    ans =0

    for i in range(a,b+1):
        i = str(i)
        if i.find(i[::-1]) == 0:
            ans +=1
     
    print(ans)

if __name__ == "__main__":
        main()
