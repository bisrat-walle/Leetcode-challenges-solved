class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        column = len(grid[0])
        is_corner = lambda i, j: i in (0, row-1) or i in (0, column-1)
        is_valid = lambda i, j: 0 <= i < row and 0 <= j < column
        an = 0
        
        def dfs(i, j):
            if not is_valid(i, j):
                return False
            if grid[i][j] == "visited" or grid[i][j] == 1:
                return True
            grid[i][j] = "visited"
            top = dfs(i+1, j)
            right = dfs(i, j+1)
            left = dfs(i, j-1)
            bottom = dfs(i-1, j)
            return top and bottom and left and right
                
        
        for i in range(row):
            for j in range(column):
                if grid[i][j] == 0 and dfs(i, j):
                    an += 1
        return an