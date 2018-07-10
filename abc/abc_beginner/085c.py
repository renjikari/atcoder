import sys

def main():
    n, y = input().split()
    n = int(n)
    y = int(y)
        
    if y % 1000 is not 0:
        print("-1 -1 -1")

    man = 0
    go = 0
    sen = 0
    lst =[man, go, sen]

    man = y // 10000
#    sentogo = n - man

    for man in range(man+1):
        sentogo = n - man

        for gosen in range(sentogo+1):
            sen = sentogo - gosen
            
            if man * 10000 + gosen * 5000 + sen * 1000 == y:
                print(man, gosen, sen)
                sys.exit()

    print("-1 -1 -1")

if __name__ == "__main__":
        main()
