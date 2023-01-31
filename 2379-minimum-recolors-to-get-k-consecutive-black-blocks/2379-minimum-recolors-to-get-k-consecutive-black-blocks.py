class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        left = 0
        ans = k
        white = 0
        for right in range(n):
            white += blocks[right] == "W"
            while right - left + 1 > k:
                white -= blocks[left] == "W"
                left += 1
            if right - left + 1 == k:
                ans = min(ans, white)
        
        return ans