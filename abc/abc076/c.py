import sys

def main():
    s = input()
    t = input()

    qlst = []
    q=0

    for i in s:
        if i == "?":
            q += 1
        elif i != "?" and q > 0:
            qlst.append(q)
            q = 0
    qlst.append(q)
    sr = s[::-1]
    print(qlst)

    # tに含まれる文字列を後ろからみつけて、まわりがいい感じか確認する
    if len(t) > max(qlst):
        for i in range(len(t)):
            for j in range(len(sr)):
                if sr[j] == "?":
                    qc +=1
                    continue
                elif sr[j] == :
 
        print("UNRESTORABLE")
        exit()


    # len(t)以上の?をみつける
    elif len(t) <= max(qlst)
        hatena = "?"*len(t)

        ans = s[::-1].replace('?'*len(t),t[::-1],1)[::-1].replace("?","a")

 
    print(ans)
    
    """
    qc = question_count = 0
    for i in range(len(t)):
        for j in range(len(sr)):
            if sr[j] == "?":
                qc +=1
                if sr[j+1] == "?" or sr[j+1] == t[i]:
                    continue
            elif j == i:
    """




if __name__ == "__main__":
        main()
