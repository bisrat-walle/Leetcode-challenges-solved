class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        @lru_cache(None)
        def dfs(row, col):
            if row == 0 and col == 0:
                return 1
            if row < 0 or col < 0:
                return 0
            
            up = dfs(row-1, col)
            left = dfs(row, col-1)
            return up + left
        
        return dfs(m-1,n-1)