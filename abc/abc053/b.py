import sys

def main():
    s = input()
        

    flag = 0
    t = ""
    u = ""

    for i in s:
        if i == "A":
            flag = 1
        if flag == 1:
            t += i

    flag = 0

    for i in t[::-1]:
        if i == "Z":
            flag = 1
        if flag ==1:
            u += i

    print(len(u))

if __name__ == "__main__":
        main()
