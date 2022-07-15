class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        is_valid = lambda i, j: 0 <= i < len(grid) and 0 <= j < len(grid[0])
        visited = set()
        drn = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        def dfs(i, j):
            visited.add((i, j))
            for i_drn, j_drn in drn:
                new_i, new_j = i + i_drn, j + j_drn
                if is_valid(new_i, new_j) and grid[new_i][new_j] == 1 and (new_i, new_j) not in visited:
                    visited.add((new_i, new_j))
                    dfs(new_i, new_j)
        an = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i, j) not in visited:
                    prev_ln = len(visited)
                    dfs(i, j)
                    new_ln = len(visited)
                    an = max(an, new_ln-prev_ln)
        
        return an