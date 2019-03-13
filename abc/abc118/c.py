import sys

def main():
    n = int(input())
    a = list(map(int,input().split()))

    while True:
        #m = find_min(a)
        m = min(a)
        #zero = 0
        for i in range(len(a)):
            if a.index(m) != i:
                a[i] = a[i] % m

        while True:
            if min(a) == 0:
                a.remove(0)
            else:
                break

        #if zero == n -1:
        if len(a) == 1:
            print(find_min(a))
            exit()

def find_min(a):
    a.sort()
    for i in a:
        if i >0:
            return i

            
      

if __name__ == "__main__":
        main()
