class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        f=0
        t=0
        for i in bills:
            if i==5:
                f+=1
            elif i==10:
                f-=1
                t+=1
            elif t>0:
                t-=1
                f-=1
            else:
                f -=3

            if f <0 :
                return False
        return True
