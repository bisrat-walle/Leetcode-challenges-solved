class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        comb = list(zip(growTime, plantTime))
        comb.sort(reverse=True)
        ans = 0
        current = 0
        for g, p in comb:
            current += p
            ans = max(ans, current + g)
        return ans
            