def main():
    h, w = input().split()
    h = int(h)
    w = int(w)

    lst =[]
    for i in range(h):
        tmp = input()
        lst.append(list(tmp))

    flag = False

    for i in range(len(lst)):
        if flag:
            break

        for j in range(len(lst[i])):
            if lst[i][j] == "#":
                if j != w - 1:
                    if lst[i][j+1] == "#":
                        continue

                if j != 0:
                    if lst[i][j-1] == '#':
                        continue

                if i != 0:
                    if lst[i-1][j] == '#':
                        continue
                       
                if i != h -1:
                    if lst[i+1][j] == '#':
                        continue

                print("No")
                flag = True
                break

    if flag == False:
        print("Yes")
    
if __name__ == "__main__":
        main()
