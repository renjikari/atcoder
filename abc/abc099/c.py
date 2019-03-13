import numpy as np

def main():
    a = input()
    a = int(a)
    b = a
    
    lst = [1, 6, 36, 216, 1296, 7776, 46656, 9, 81, 729, 6561, 59049]

    lst = np.sort(lst)[::-1]
    #[59049 46656  7776  6561  1296   729   216    81    36     9     6     1]
    use = [0] *12

    ans = 0

    while a > 0:
        for i in range(12):
            if a >= lst[i]:
                a = a - lst[i]
                ans+=1
                use[i] = use[i] + 1
                break

#    print(use)
    print(ans)


"""
    for i in use:
        if i > 0:
            big = use.index(i)
            print(use.index(i))
            break
"""            
"""
    while b >0:
        for i in range(12):
            if a>= lst[i]:

                a = a -lst[i]
                ans+=1
                break
"""

if __name__ == "__main__":
        main()
