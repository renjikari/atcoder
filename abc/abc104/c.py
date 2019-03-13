import sys

def main():
    d, g = map(int,input().split())
    D = list(range(100,d*100+1,100))
    
    p = []
    c = []

    for i in range(d):
        P, C = map(int,input().split())
        p.append(P)
        c.append(C)


    pall =[]

    for i in range(d):
        pall.append([p[i],p[i]*100*(i+1) + c[i]])

    print(pall)

    #print(D)
    #print(list(enumerate(pall)))
    #pall = list(enumerate(pall))
    #pall = list(reversed(sorted(pall, key=lambda x: x[1])))

    """
    for i in range(d):
        pall[i] = list(pall[i])
        print(pall[i][0])
        #print(g[pall[i][0]])
        pall[i].append(p[pall[i][0]])

    print(pall)
    """

    dp=[0]*2000
    dp[0]=0
    z =0

    D = D[::-1]
    p_rev = p[::-1]

    """
    for i in range(d):

        while i > 0:
            tmp = dp[z] + D[i]
            if z+1 in p:
                dp[z+1] = max(tmp, (p.index(z+1)+1)*100 + c[p.index(z+1)] )
            else:
                dp[z+1] = tmp

            if dp[z+1] >= g:
                print(z+1)
                exit()

            p[i]-=1
    """

        

if __name__ == "__main__":
        main()
