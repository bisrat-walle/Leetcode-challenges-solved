class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = [None, None]
        found = False;
        for i in range(len(nums)):
            answer[0] = i
            for j in range(i+1, len(nums)):
                if (nums[i] + nums[j]) ==  target:
                    answer[1] = j
                    return  answer
        

sol = Solution()
print(sol.twoSum([2,7,11,15], 9))