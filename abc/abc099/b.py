import sys

def main():
    a, b = input().split()
    a = int(a)
    b = int(b)
        

    sa = b - a

    lst =[0]

    for i in range(1,1000):
        lst.append(lst[-1]+i)

    print(lst[sa] - b)



if __name__ == "__main__":
        main()
