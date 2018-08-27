import sys

def main():
    a = int(input())

    ans = 0
    for i in range(a):
        ans = max(ans, i *(a-i))

    print(ans)
    
    
if __name__ == "__main__":
        main()
