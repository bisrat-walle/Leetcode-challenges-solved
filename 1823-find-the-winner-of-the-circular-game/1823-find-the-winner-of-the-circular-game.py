class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = list(range(1, n + 1))
        length = len(arr)
        ref = 0

        while arr:
            rem = (ref + k - 1) % length
            ans = arr.pop(rem)
            ref = rem
            length -= 1
        
        return ans