class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        """
        [2, 3, 4, 5]
        [2, 4, 5, 9]
        
        
        """
        nums.sort()
        n = len(nums)
        ans = 0
        i = 0
        half = math.ceil(n//2)
        for j in range(math.ceil(n/2), n):
            if 2 * nums[i] <= nums[j]:
                ans += 2
                i += 1
                
        return ans
        