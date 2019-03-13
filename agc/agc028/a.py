def main():
    n, m = map(int,input().split())
    s = input()
    t = input()
  
    l = n * m // gcd(n,m)
    
    nlist = [0 for i in range(n)]
    mlist = [0 for i in range(m)]
    for i in range(n):
        nlist[i] =  i*l//n

    for i in range(m):
        mlist[i] =  i*l//m

    src_set = set(nlist)
    tag_set = set(mlist)
    matched_list = list(src_set.intersection(tag_set))

    for i in matched_list:
        s_index = nlist.index(i)
        t_index = mlist.index(i)

        if s[s_index] != t[t_index]:
            print("-1")
            exit()

    print(l)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

if __name__ == "__main__":
        main()
