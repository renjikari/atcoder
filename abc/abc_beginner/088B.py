import numpy as np

def main():
    N = input()
    a = input().split()

    N = int(N)
    # a = list(map(int,a))
    a = np.array([int(a) for a in a])
    a = np.sort(a)[::-1]

    alice = []
    bob = []

    for i in range(N):
        if i % 2:
            bob.append(a[i])
        else:
            alice.append(a[i])

    ans = sum(alice) - sum(bob)

    print(ans)

if __name__ == "__main__":
        main()
