import sys
def main():
    x = input()
    x = int(x)
        
    ans = 0

#    x = x - 5
#    ans += 1
    
    ans += (x // 11) *2
    x = x % 11
    if x == 0:
        print(ans)
        exit()

    ans += x//6
    x = x % 6
    if x == 0:
        print(ans)
    else:
        ans += 1
        print(ans)

if __name__ == "__main__":
        main()
