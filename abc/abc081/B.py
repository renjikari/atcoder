import numpy as np

def main():
    N = input()
    a = input().split()

    N = int(N)
    #a = list(map(int,a))
    zero_lst = [0] * N 
    a = np.array([int(a) for a in a])
    ans = 0;

    for i in range(30):
        if np.allclose(zero_lst, a % 2):
            a = a/2
            ans+=1
        else:
            break

    print(ans)

if __name__ == "__main__":
        main()
