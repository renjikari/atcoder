s = input()
n = len(s)

if n %2 ==0:
    if s[0] == s[-1]:
        print("First")
    else:
        print("Second")
else:
    if s[0] == s[-1]:
        print("Second")
    else:
        print("First")

