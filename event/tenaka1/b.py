import sys

def main():
    a, b, k = map(int,input().split())


    for i in range(k):
        if i % 2 == 0:
            if a % 2 == 1:
                a = a-1
            b = b+ a//2
            a = a//2
        
        else:
            if b % 2 == 1:
                b = b-1
            a = a + b//2
            b = b//2

    print(str(a) +" "+str(b))



       

if __name__ == "__main__":
        main()
