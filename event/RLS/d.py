import sys

def main():
    s = input()

    if len(s) ==1:
        print(0)

    ans_lst = []
    for i in range(1,len(s)):
        ans_lst.append(split(s,i))

    print(ans_lst)


def split(s, n):
    if len(s) ==1:
        print("len 1")
        return 0
    else:
        l = s[:n]
        r = s[n:]
        print(l)
        print(r)

        l_ans =[]
        r_ans=[]
        if len(l) ==1:
            l_ans.append(0)
        if len(r) ==1:
            r_ans.append(0)

        for i in range(1,len(l)):
            l_ans.append(split(l,i))

        for i in range(1,len(r)):
            r_ans.append(split(l,i))

        #print(int(l[-1])*len(l))
        #print(int(r[0])*len(r))
        print(l_ans)
        print(r_ans)
        return int(l[-1])*len(l) + int(r[0])*len(r) + min(l_ans) + min(r_ans)
    
       

if __name__ == "__main__":
        main()
