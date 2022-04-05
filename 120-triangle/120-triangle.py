class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        @lru_cache(None)
        def dp(row=0, index=0):
            if row == len(triangle)-1:
                return triangle[-1][index]
            pathsum1 = triangle[row][index] + dp(row+1, index)
            pathsum2 = triangle[row][index] + dp(row+1, index+1)
            return min(pathsum1, pathsum2)
        return dp()