class stack:
    def __init__(self):
        self.stack = []
    def push_(self,val):
        self.stack.append(val)
        
    def mid(self):
        if not self.stack:
            return None
        else:
            mid = len(self.stack)//2
            print(self.stack.pop(mid))
    def display(self):
        print(self.stack)
s=stack()
s.push_(10)
s.push_(20)
s.push_(30)
s.push_(40)
s.push_(50)
s.display()
s.mid()
s.display()
