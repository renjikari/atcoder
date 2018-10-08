import sys

def main():
    x = int(input())
    
    ans = 0
    c = 0
    for i in range(1,100000000):
        ans+=1
        c +=i
        if c >= x:
            print(ans)
            exit()



if __name__ == "__main__":
        main()
