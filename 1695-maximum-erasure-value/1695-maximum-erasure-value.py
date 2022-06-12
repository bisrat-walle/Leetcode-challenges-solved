class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        i, j = 0, 0
        current_sum = 0
        set_list = set()
        an = float("-inf")
        while j < len(nums):
            if nums[j] not in set_list:
                current_sum += nums[j]
                an = max(current_sum, an)
            else:
                while nums[i] != nums[j]:
                    current_sum -= nums[i]
                    set_list.remove(nums[i])
                    i += 1
                i += 1
            set_list.add(nums[j])
            j += 1
        return an