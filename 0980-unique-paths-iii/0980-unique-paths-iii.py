class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        starting, ending = None, None
        obstacles = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    starting = i, j
                elif grid[i][j] == 2:
                    ending = i, j
                elif grid[i][j] == -1:
                    obstacles += 1
        
        non_obstacles = n*m - obstacles
                    
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        is_valid = lambda i, j: 0 <= i < n and 0 <= j < m and grid[i][j] != -1
        
        visited = {starting}
        current_non_obstacles = 1
        ans = 0
        def backtrack(i, j):
            nonlocal ans, current_non_obstacles
            if (i, j) == ending:
                ans += current_non_obstacles == non_obstacles
                return 
            for i_drn, j_drn in directions:
                new_i, new_j = i + i_drn, j + j_drn
                if is_valid(new_i, new_j) and (new_i, new_j) not in visited:
                    visited.add((new_i, new_j))
                    current_non_obstacles += 1
                    backtrack(new_i, new_j)
                    visited.discard((new_i, new_j))
                    current_non_obstacles -= 1
        
        backtrack(*starting)
        return ans
                