a,b,c,d,e = map(int,input().split())

lst = []
lst.append(a+b+c)
lst.append(a+b+d)
lst.append(a+b+e)
lst.append(a+c+d)
lst.append(a+c+e)
lst.append(a+d+e)
lst.append(b+c+d)
lst.append(b+c+e)
lst.append(b+d+e)
lst.append(c+d+e)


print(max(a+d+e,b+c+d))
