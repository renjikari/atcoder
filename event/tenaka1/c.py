import itertools

def main():
    n = int(input())

    lst = [0 for i in range(n)]
    for i in range(n):
        lst[i] = int(input())

    lst = sorted(lst)
       

    # -(-n//2) => 切り上げ
    if n %2 == 0:
        lst1 = lst[0:-(-n//2)]
        lst2 = lst[-(-n//2):n]

        lst1 = list(itertools.permutations(lst1))
        #lst2 = list(itertools.permutations(lst2))

        ans = 0
        l2 = lst2
        for l1 in lst1:
            #for l2 in lst2:
            ans = max(ans,calc(n,l1, l2))

        print(ans)

    else:
        lst2A = list(itertools.permutations(lst[n//2:n]))
        lst1B = list(itertools.permutations(lst[0:-(-n//2)]))

        ans = 0

        l1 = lst[0:n//2]
        for l2 in lst2A:
            ans = max(ans,calcA(l1, l2))

        l2 = lst[-(-n//2):n]
        for l1 in lst1B:
            ans = max(ans,calc(n, l1, l2))

        print(ans)

def calc(n,lst1,lst2):
    ret = 0
    if n %2 == 1:
        for i in range(len(lst2)):
            ret += lst2[i] - lst1[i]
            ret += lst2[i] - lst1[i+1]
    else:
        for i in range(n//2):
            ret += lst2[i] - lst1[i]
            if not i == len(lst2)-1:
                ret += lst2[i+1] - lst1[i]
    return ret

def calcA(lst1,lst2):
    ret=0
    for i in range(len(lst1)):
        ret += lst2[i] - lst1[i]
        ret += lst2[i+1] - lst1[i]

    return ret



if __name__ == "__main__":
        main()
