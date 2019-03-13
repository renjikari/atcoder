
class fifo():
    
    lst =[]
    #def _init_:
    #    pass

    def push(self, n):
        self.lst.insert(0,n)

    def pop(self):
        #return self.lst.pop()
        #return self.lst.remove(-1)
        ret = self.lst[-1]
        del self.lst[-1]
        return ret

    def get(self):
        return self.lst


a = fifo()
a.push(1)
a.push(2)
a.push(3)

print(a.get())
print(a.pop())
print(a.get())
