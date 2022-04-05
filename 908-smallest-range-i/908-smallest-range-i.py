class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        substracted = [i-k for i in nums]
        added = [i+k for i in nums]
        return max(max(substracted)-min(added), 0)
        