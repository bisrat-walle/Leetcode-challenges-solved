class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        left = 1
        right = x
        while left < right:
            mid = (left + right + 1)//2
            if mid ** 2 > x:
                right = mid - 1
            else:
                left = mid
        return left