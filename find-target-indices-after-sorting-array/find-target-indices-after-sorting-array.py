class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        an = []
        nums = sorted(nums)
        for i in range(len(nums)):
            if nums[i] == target:
                an.append(i)
        return an
        