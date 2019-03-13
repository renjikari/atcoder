import sys

def main():
    S = list(input().strip(".").split())

    ans = 0
    for word in S:
        if "{" in word:
            ans += len(max(word.strip("{").strip("}").split(","), key=len))
        else:
            ans += len(word)


    print(ans/len(S))

if __name__ == "__main__":
        main()
