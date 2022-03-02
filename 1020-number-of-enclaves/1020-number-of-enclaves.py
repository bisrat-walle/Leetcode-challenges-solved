class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        
        
        
        def dfs(i, j):
            if (i, j) in visited:
                return
            if grid[i][j] == 1:
                visited.append((i, j))
                if i >= 1:
                    dfs(i-1, j)
                if i < len(grid)-1:
                    dfs(i+1, j)
                if j >= 1:
                    dfs(i, j-1)
                if j < len(grid[0])-1:
                    dfs(i, j+1)
        
        visited = []
        ones = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    ones += 1
                    
                    if i == 0 or i == len(grid)-1 or j == 0 or j == len(grid[0])-1:
                        if (i,j) not in visited:
                            dfs(i, j)
        # print(visited, ones)
        return ones - len(visited)
            