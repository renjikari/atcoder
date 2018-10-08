import sys

def main():
    n = int(input())
    a =[0 for i in range(n)]
    
    for i in range(n):
        a[i] = [i, int(input())]

    lst = sorted(a,key=lambda x: x[1])

    tmp = lst[0][1]
    compression = 0
    for i,j in lst:
        if tmp < j:
            compression+=1
            tmp = j

        a[i][1] = compression
        
    
    for i,j in a:
        print(j)
       

if __name__ == "__main__":
        main()
