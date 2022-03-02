class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        
        
        visited = set()
        
        
        def dfs(i, j):
            if (i, j) in visited or grid[i][j] == 0:
                return 0
            area = 1
            if grid[i][j] == 1:
                visited.add((i, j))
                if i >= 1:
                    area += dfs(i-1, j)
                if i < len(grid)-1:
                    area += dfs(i+1, j)
                if j >= 1:
                    area += dfs(i, j-1)
                if j < len(grid[0])-1:
                    area += dfs(i, j+1)
            # print(f"Area from {i, j} is {area}")
            return area
        
        max_area = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    if (i,j) not in visited:
                        max_area = max(dfs(i, j), max_area)
        
        # print(visited)
        return max_area