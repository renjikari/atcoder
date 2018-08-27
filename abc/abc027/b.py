import sys

def main():
    n = int(input())
    lst = list(map(int,input().split()))
    s = sum(lst)

    if s % n !=0:
        print(-1)
        exit()

    live = s / n 
    island_num = 0
    ans = 0
    human_num = 0

    for i in lst:
        island_num += 1
        if  i+human_num == live * island_num:
            island_num = 0
            human_num = 0

        else:
            human_num += i
            ans +=1

    print(ans)

           
if __name__ == "__main__":
        main()
