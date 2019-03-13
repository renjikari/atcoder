import statistics

def main():
    n = int(input())

    lst = [0 for i in range(n)]
    for i in range(n):
        lst[i] = list(map(int,input().split()))

    zero = False
    for i in range(n):
        if lst[i][2] != 0:
            break
        if i == n-1:
            zero = True

    if zero == True:
        for i in range(101):
            for j in range(101):
                h = []
                h_ij =[]
                for k in range(n):
                    tmp = lst[k][2] + abs(lst[k][0] - i) + abs(lst[k][1] - j)
                    h.append(tmp)
                    h_ij.append([i,j])

                    if k == n-1:
                        high = statistics.mode(h)
                        print(str(h_ij[h.index(h)][0])+ " " + str(h_ij[h.index(h)][1]) + " " + str(high))
   
       
    for i in range(101):
        for j in range(101):
            remain = []
            remain_flag = False
            for k in range(n):
                if k == 0 or remain_flag:
                    if lst[k][2] == 0:
                        remain.append(lst[k])
                        remain_flag = True
                        continue

                    h = lst[k][2] + abs(lst[k][0] - i) + abs(lst[k][1] - j)
                    remain_flag = False
                    continue

                if max(h - abs(lst[k][0] - i) - abs(lst[k][1] - j),0) == lst[k][2]:
                    if k == n-1:
                        for remain in remain:
                            if max(h - abs(remain[0] - i) - abs(remain[1] - j),0) != remain[2]:
                                break

                        print(str(i)+ " " + str(j) + " " + str(h))
                        exit()
                    continue
                else:
                    break


if __name__ == "__main__":
        main()
