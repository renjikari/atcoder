import sys

def main():
    a,b,c,d,e,f= map(int,input().split())
        
    # 100gあたりE [g]溶ける
    # ビーカーにF [g]いれられる
    # 濃度は100*砂糖 / (水＋砂糖)


    mizu=[]
    sato=[]


    x = int(f/100/a) +1
    y = int(f/100/b) +1

    for i in range(x):
        for j in range(y):
            mizu.append(i*100*a + j*100*b)

    mizu = [i for i in mizu if i <= f]
    mizu = list(set(mizu))
    mizu.sort()

    tokeru = int(f/100) * e
    x = int(tokeru / c) +1
    y = int(tokeru / d) +1

    for i in range(x):
        for j in range(y):
            sato.append(i*c + j*d)

    sato = [i for i in sato if i < tokeru]
    sato = list(set(sato))
    sato.sort()
#    sato.remove(0)
#    mizu.remove(0)

    tmp =0
    
    for i in mizu:
        for j in sato:
            if i + j <= f and i + j !=0:
                if int(i/100)*e >=j:
                    if tmp <= (100*j) / (i + j):
                        tmp = (100*j) / (i + j)
                        ans = str(i+j) + " " + str(j)
    
    print(ans)


if __name__ == "__main__":
        main()
