class Solution:
    def sumZero(self, n: int) -> List[int]:
        arr = []
        if n%2:
            arr.append(0)
            n -= 1
        
        left, right = -1, 1
        
        while n:
            arr.append(left)
            arr.append(right)
            left -= 1
            right += 1
            n -= 2
        
        
        return arr