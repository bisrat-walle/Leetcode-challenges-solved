class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        min_ = min(nums)
        max_ = max(nums)
        for i in range(len(nums)):
            if nums[i] == min_:
                min_index = i

            if nums[i] == max_:
                max_index = i
        option1 = min(max_index+1, len(nums)-max_index) + min(min_index+1, len(nums)-min_index)
        earlier = min(min_index, max_index)
        later = max(min_index, max_index)
        return min(later+1, len(nums)-earlier, option1)