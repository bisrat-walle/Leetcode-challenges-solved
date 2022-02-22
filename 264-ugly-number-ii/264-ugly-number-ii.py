class Solution:
    def nthUglyNumber(self, n: int) -> int:
        an = [1] + [0]*(n-1)
        p2, p3, p5 = 0, 0, 0
        mult2, mult3, mult5 = 2, 3, 5
        
        for i in range(1, n):
            an[i] = min(mult2, mult3, mult5)               
                                                     
            if an[i] == mult2:                           
                p2+=1
                mult2 = an[p2] * 2
            if an[i] == mult3:                           
                p3+=1                                
                mult3 = an[p3] * 3  
            if an[i] == mult5:                           
                p5+=1                                
                mult5 = an[p5] * 5
        return an[-1]