class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        ans = 0
        for bit in range(31, -1, -1):
            count = 0
            for candidate in candidates:
                if candidate & 2**bit:
                    count += 1
            ans = max(ans, count)
        
        return ans