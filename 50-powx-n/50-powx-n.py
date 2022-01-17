class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n==1: 
            return x
        elif n==-1:
            return 1/x
        else:
            if n>1:
                if n%2 == 0:
                    temp = self.myPow(x, n//2)
                    return temp**2
                return x *  self.myPow(x, n-1)
            if n%2 == 0:
                temp = self.myPow(x, n//2)
                return (temp)**2
            return (1/x)*self.myPow(x, n+1)
       