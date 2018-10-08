import sys

def main():
    s = input()


    ans = 0
    now = ""
    for i in s:
        if now != i:
            ans +=1
            now = i

    print(ans -1)




if __name__ == "__main__":
        main()
