from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        queue = deque()
        visited = set()
        
        if grid[0][0] == 0:
            queue.append((1, (0, 0)))
            visited.add((0, 0))
        
        dirs = [[1,0],[-1,0],[0,1],[0,-1],[1,-1],[-1,1],[1,1],[-1,-1]]
        
        while queue:
            step, (r, c) = queue.popleft()
            if r == m - 1 and c == n - 1:
                return step
            for i, j in dirs:
                new_r, new_c = r+i, c+j
                if 0 <= new_r < m and 0 <= new_c < n and not grid[new_r][new_c] and (new_r, new_c) not in visited:
                    queue.append((step+1, (new_r, new_c)))
                    visited.add((new_r, new_c))
        return -1