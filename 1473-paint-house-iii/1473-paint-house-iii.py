class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        
        @lru_cache(None)
        def getMin(index=0, neighborhoods=0, prevcolor=None):
            if (index == m and neighborhoods != target) or neighborhoods > target:
                return float("inf")
            
            if index == m:
                return 0
            
            if houses[index] != 0:
                mincost = getMin(index+1, neighborhoods+int(prevcolor != houses[index]), houses[index])
            else:
                mincost = float("inf")
                for color, cos in enumerate(cost[index], 1):
                    mincost = min(mincost, cos + getMin(index+1, neighborhoods+int(prevcolor != color),\
                                                        color))
            return mincost
        
        res = getMin()
        return res if res != float("inf") else -1
    