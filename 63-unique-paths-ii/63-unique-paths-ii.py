class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[-1][-1] == 1 or obstacleGrid[0][0] == 1:
            return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        @lru_cache(None)
        def dfs(row, col):
            if row == 0 and col == 0:
                return 1
            if row < 0 or col < 0:
                return 0
            up = left = 0
            if obstacleGrid[row-1][col] == 0:
                up = dfs(row-1, col)
            if obstacleGrid[row][col-1] == 0:
                left = dfs(row, col-1)
            return up + left
        
        return dfs(m-1,n-1)