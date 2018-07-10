def main():
    n = input()
    kokuban = input().split()
    kokuban = list(map(int, kokuban))

    ans = 0
    flag = False

    while True:
        for i in kokuban:
            if i % 2 is 1:
                flag = True

        if flag:
            break
 
        kokuban = [x//2 for x in kokuban]
        ans += 1

    print(ans)
      
if __name__ == "__main__":
        main()
