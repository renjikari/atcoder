import sys
import numpy as np

def main():
    n, k = map(int,input().split())
    lst = list(map(int,input().split()))
    arr = np.array(lst)

    if np.any(arr == 0):
        if k == 1:
            print(0)
            exit()
        k -= 1

    plus = arr[np.where(arr>0)]
    len_plus = len(plus)
    plus = np.insert(plus,0,0)
    minus = arr[np.where(arr<0)][::-1]
    len_minus = len(minus)
    minus = np.insert(minus,0,0)

   # print(plus)
    #print(len_plus)
    #print(plus[len_plus])
    #print(minus)
    #print("#######")

    anslist = []
    ans = 100000000000000000000


    for i in range(k):
        if len_plus < k:
            try:
                ans = plus[len_plus-i] + (abs(minus[i+(k-len_plus)])*2)
                anslist.append(ans)
            except:
                break

        elif len_plus >= k:
            try:
                ans = plus[k-i] + (abs(minus[i])*2)
                #print(ans)
                anslist.append(ans)
            except:
                break
            
    for i in range(k):
        if len_minus < k:
            try:
                ans = abs(minus[len_minus-i]) + (plus[i+(k-len_minus)]*2)
                anslist.append(ans)
            except:
                break
        else:
            try:
                ans = abs(minus[k-i]) + (plus[i]*2)
                anslist.append(ans)
            except:
                break
 
 
    #print(anslist)
    print(min(anslist))



if __name__ == "__main__":
        main()
