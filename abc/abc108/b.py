import sys

def main():
    lst = list(map(int,input().split()))

    x= lst[2] - lst[0] 
    y= lst[3] - lst[1] 

    #print(lst[1]-y)
    #print(lst[3]+x)

    x3 = lst[2]-y
    y3 = lst[3]+x

    x4 = x3 - x 
    y4 = y3 - y

    print(str(x3) +" "+ str(y3)+" "+str(x4)+" "+str(y4))
       

if __name__ == "__main__":
        main()
