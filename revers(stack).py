class stack:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def push_(self,val):
        self.stack1.append(val)
    def revers(self):
        if not self.stack1:
            print("None")
        else:
            while self.stack1:
                val=self.stack1.pop()
                self.stack2.append(val)
    def display1(self):
        print("after",self.stack2)
    def display2(self):
        print("before",self.stack1)
s=stack()
s.push_(5)
s.push_(4)
s.push_(3)
s.push_(2)
s.push_(1)
s.display2()
s.revers()
s.display1()
