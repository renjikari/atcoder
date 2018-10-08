import sys

def main():
    n = int(input())

    S = [0 for i in range(n)]
    for i in range(n):
        S[i] = input()

    
    lst =[0,0,0,0,0]
    for i in S:
        if i[0] == "M":
            lst[0]+=1
        if i[0] == "A":
            lst[1]+=1
        if i[0] == "R":
            lst[2]+=1
        if i[0] == "C":
            lst[3]+=1
        if i[0] == "H":
            lst[4]+=1

    ans =0
    ans += lst[0] * lst[1] * lst[2]   
    ans += lst[0] * lst[1] * lst[3]   
    ans += lst[0] * lst[1] * lst[4]   
    ans += lst[0] * lst[2] * lst[3]   
    ans += lst[0] * lst[2] * lst[4]   
    ans += lst[0] * lst[3] * lst[4]   
    ans += lst[1] * lst[2] * lst[3]   
    ans += lst[1] * lst[2] * lst[4]   
    ans += lst[1] * lst[3] * lst[4]   
    ans += lst[2] * lst[3] * lst[4]   

    print(ans)
       

if __name__ == "__main__":
        main()
