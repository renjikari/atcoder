import sys
import itertools

def main():
    B =[]
    C =[]
    for i in range(2):
        tmp = input().split()
        B.append(tmp)

    for i in range(3):
        tmp = input().split()
        C.append(tmp)


    print(B)
    print(C)

    dai = 0
    ko = 0

    seq = (0,1,2,3,4,5,6,7,8)
    lst = list(itertools.combinations(seq,5))

    for i in lst:
        for b in B[0]:
            if b != 0:
                if B[0].index(b) in i and B[1].index(b) in i:
                    dai += b
                elif B[0].index(b) not in i and B[1].index(b) not in i:
                    dai += b
                else:
                    ko += b
        for b in B[1]:
            if b != 0:
                if B[1]
        for c in C[0]:



    for i in range():
        marubstu[i][j]=0

if __name__ == "__main__":
        main()
