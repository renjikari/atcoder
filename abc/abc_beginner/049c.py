import sys
sys.setrecursionlimit(10000)

n = 0
lst = ["dream", "dreamer", "erase", "eraser"]

def main():
    a = input()
    global n
    n = len(a)

    if a[0] == "e":
        erase(0,a)
    elif a[0] == "d":
        dream(0,a)
    else:
        print("NO")


def erase(i,a):
    if i+5==n:
        if a[i:i+5] in lst:
            print("YES")
            sys.exit()

    if i+6==n:
        if a[i:i+6] in lst:
            print("YES")
            sys.exit()
 
    if i+7==n:
        if a[i:i+7] in lst:
            print("YES")
            sys.exit()
 

    if a[i:i+5] == "dream":
        if a[i+5] == "d":
            print(1)
            dream(i+5,a)

    if a[i:i+5] == "erase":
        if a[i+5] is "d":
            dream(i+5, a)

        elif a[i+5] == "e":
            erase(i+5, a)

        elif a[i+5] == "r":
            if a[i+6] == "e":
                erase(i+6, a)
            elif a[i+6] == "d":
                dream(i+6, a)
            else:
                print("NO")
                sys.exit()
        else:
            print("NO")
            sys.exit()
    
    print("NO")
    sys.exit()


def dream(i,a):
    if i+5==n:
        if a[i:i+5] in lst:
            print("YES")
            sys.exit()

    if i+6==n:
        if a[i:i+6] in lst:
            print("YES")
            sys.exit()
 
    if i+7==n:
        if a[i:i+7] in lst:
            print("YES")
            sys.exit()
 
    if a[i:i+5] == "dream":
        if a[i+5] == "d":
            dream(i+5,a)

        elif a[i+5] == "e":
            # dreamerase
            if a[i+7] == "a":
                erase(i+5, a)

            # dreamererase
            elif a[i+7] == "e":
                erase(i+7, a)

            # dreamerdream
            elif a[i+7] == "d":
                dream(i+7, a)

            else:
                print("NO")
                sys.exit()
        else:
            print("NO")
            sys.exit()
 
    print("NO")
    sys.exit()
       
if __name__ == "__main__":
        main()
