from collections import Counter

def main():
    n = int(input())
    v = list(map(int,input().split()))

    if len(set(v)) == 1:
        print(len(v)//2)
        exit()


    ans = 0 
    vc = Counter(v)
    vc0 = Counter(v[::2])
    vc1 = Counter(v[1::2])

    if len(set(v[::2])) == 1:
        if v[0] == vc1.most_common(1)[0][0]:
            print(vc1.most_common(1)[0][1])
        else:
            print(len(v)//2 - vc1.most_common(1)[0][1])

        exit()
    elif len(set(v[1::2])) == 1:
        if v[1] == vc0.most_common(1)[0][0]:
            print(vc0.most_common(1)[0][1])
        else:
            print(len(v)//2 - vc0.most_common(1)[0][1])
        exit()

    if vc.most_common(1)[0][1] >= len(v)//2:
        if vc0.most_common(2)[1][1] > vc1.most_common(2)[1][1]:
            if len(set(v[::2])) !=1:
                ans += len((v[::2])) - vc0.most_common(2)[1][1]
            ans += len((v[1::2])) - vc1.most_common(1)[0][1]
        else:
            ans += len((v[::2])) - vc0.most_common(1)[0][1]
            if len(set(v[1::2])) !=1:
                ans += len((v[1::2])) - vc1.most_common(2)[1][1]

    else:
        ans += len((v[::2])) - vc0.most_common(1)[0][1]
        ans += len((v[1::2])) - vc1.most_common(1)[0][1]

    print(ans)

if __name__ == "__main__":
        main()
