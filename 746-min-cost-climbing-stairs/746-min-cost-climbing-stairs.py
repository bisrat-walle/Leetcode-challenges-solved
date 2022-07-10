class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        last = cost[-1]
        before_last = cost[-2]
        n = len(cost)
        
        for i in reversed(range(n-2)):
            res = cost[i] + min(before_last,last)
            last = before_last
            before_last = res
        return min(before_last,last)