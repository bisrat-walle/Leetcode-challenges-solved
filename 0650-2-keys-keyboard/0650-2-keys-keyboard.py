class Solution:
    def minSteps(self, n: int) -> int:
        written = 1
        prev = 1
        rem = n-1
        op = 0
        while written < n:
            if rem%written == 0:
                op += 2
                prev = written
                written += written
            else:
                op += 1
                written += prev
            
            rem = n - written
                
        return op