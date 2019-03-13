def main():
    n = int(input())
    a = list(map(int,input().split()))
  
    while True:
        m = min(a)
        new = [0 for i in range(n)]
        new[0] = m

        ind=1
        for i in range(len(a)):
            if a.index(m) != i:
                num = a[i]%m
                if num != 0:
                    new[ind] = a[i]%m
                    ind+=1

        a = new[:ind]
        print(a)
  
        if len(a) == 1:
            print(min(a))
            exit()

     
     
     
if __name__ == "__main__":
    main()
