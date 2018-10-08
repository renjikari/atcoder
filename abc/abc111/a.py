import sys

def main():
    n = list(input())

    ans = ""
    for i in n:
        if i == "1":
            ans+= "9"
        if i == "9":
            ans+= "1"

    print(ans)
       

if __name__ == "__main__":
        main()
