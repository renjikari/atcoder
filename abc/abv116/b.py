import sys

def main():
    s = int(input())

    an = s
    lst = [an]
    tmp = 10000001

    i = 1
    while True:
        i+=1
        if an%2  == 0:
            an = an/2
            tmp = an
            if tmp in lst:
                print(i)
                exit()

            lst.append(an)

        else:
            an = an*3+1
            tmp = an
            if tmp in lst:
                print(i)
                exit()

            lst.append(an)
       

if __name__ == "__main__":
        main()
