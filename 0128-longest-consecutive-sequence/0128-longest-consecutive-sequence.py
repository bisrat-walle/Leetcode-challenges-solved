class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        ans = 0
        for num in nums:
            if num+1 not in nums_set:
                num_cpy = num
                current = 1
                while num_cpy-1 in nums_set:
                    num_cpy -= 1
                    current += 1
                ans = max(ans, current)
                # print(num, current)
        return ans