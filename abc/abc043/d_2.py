s = input()

if len(s) == 2:
    if len(set(list(s))) == 1:
        print("1 2")
        exit()

for i in range(len(s)-2):
    if len(set(list(s[i:i+3]))) != 3:
        print(str(i+1)+ " "+ str(i+3))
        exit()

print("-1 -1")



