import sys

def main():
    s = input()
    k = int(input())

    if len(s) < k:
        print(0)
        exit()

    anslst = []

    for i in range(len(s)-k+1):
        anslst.append(s[i:i+k])

    print(len(set(anslst)))

if __name__ == "__main__":
        main()
