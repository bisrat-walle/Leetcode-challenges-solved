from collections import defaultdict

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
            
        @lru_cache(None)
        def maxPoints(num):
            if num == 0:
                return 0
            if num == 1:
                return points[1]
            option1 = maxPoints(num-2)+points[num]
            option2 = maxPoints(num-1)
            return max(option2, option1)
        
        points = defaultdict(int)
        max_num = float("-inf")
        for num in nums:
            max_num = max(max_num, num)
            points[num] += num
            
        return maxPoints(max_num)