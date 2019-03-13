import sys

def main():
    a = input()
    b, c = input().split()
    char = input()
    a = int(a)
    b = int(b)
    c = int(c)
        
    print(str(a+b+c) + " " + char)

    """
    if N == 0 and M == 0:
        sys.exit()
    lst = input().split()
    ans = func(N, M, lst)
    print(ans)
    """

def func(N, M, lst):
    al = []
    #print(lst)
    lst1 = list(map(int, lst))
    lst2 = list(map(int, lst))
    #print(lst)

    for i in range(len(lst1)): 
        for j in range(len(lst2)):
            if not i == j:
                al.append(lst1[i] + lst2[j])
    ans = 0
    for a in al:
        if a > ans and a <= M:
            ans = a;

    if ans == 0:
        ans = "NONE"
    return ans


if __name__ == "__main__":
        main()
