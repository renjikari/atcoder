import sys

def main():
    N = input()
    N = int(N)

    S = input()
        
    x = 0
    lst =[0]

    for i in S:
        if i == "I":
            x +=1
        else:
            x -=1
        lst.append(x)

    print(max(lst))

if __name__ == "__main__":
        main()
