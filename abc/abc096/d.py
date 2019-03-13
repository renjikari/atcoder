import sys

def main():
    n = input()
    n = int(n)

    lst = prime()

    ans = ""
    for i in range(n):
        ans = ans + str(lst[i]) + " " 

    ans = ans.rstrip()
    ans = ans + "'"

    print(ans)

def prime():
    counter = 0
    primes = [2, 3]

    for n in range(5, 2000, 2):
        isprime = True
        for i in range(1, len(primes)):
            counter += 1
            if n % primes[i] == 0:
                isprime = False
                break
        if isprime:
            if n % 5 == 1:
                primes.append(n)
        if len(primes) > 70:
            break
    primes.remove(2)
    primes.remove(3)

    return primes


if __name__ == "__main__":
        main()
