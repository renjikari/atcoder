import sys

def main():
    n = int(input())
    b = [0]
    for i in range(n-1):
        b.append(int(input()))

    salary = [1]*n

    for i in range(n)[::-1]:
        if i+1 in b:
            tmp = []
            for j in range(n):
                if b[j] == i+1:
                    tmp.append(salary[j])

            salary[i] = max(tmp)+min(tmp)+1

        else:
            salary[i] = 1

    print(salary[0])



if __name__ == "__main__":
        main()
