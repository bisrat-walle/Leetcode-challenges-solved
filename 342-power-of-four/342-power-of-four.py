class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        ch = [4**i for i in range(16)]
        return n in ch
        