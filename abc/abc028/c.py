import sys

def main():
    n = list(map(int,input().split()))


    lst =[]
    lst.append(n[0]+n[1]+n[2])
    lst.append(n[0]+n[1]+n[3])
    lst.append(n[0]+n[1]+n[4])
    lst.append(n[0]+n[2]+n[3])
    lst.append(n[0]+n[2]+n[4])
    lst.append(n[0]+n[3]+n[4])
    lst.append(n[1]+n[2]+n[3])
    lst.append(n[1]+n[2]+n[4])
    lst.append(n[1]+n[3]+n[4])
    lst.append(n[2]+n[3]+n[4])


    print(sorted(lst)[-3])

if __name__ == "__main__":
        main()
