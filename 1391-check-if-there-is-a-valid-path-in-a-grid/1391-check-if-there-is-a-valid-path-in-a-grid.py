class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        drn = {
            1: [(0, -1), (0, 1)] ,
            2: [(-1, 0), (1, 0)] ,
            3: [(0, -1), (1, 0)] ,
            4: [(0, 1), (1, 0)] ,
            5: [(0, -1), (-1, 0)] ,
            6: [(0, 1), (-1, 0)] ,
        }
        
        n, m = len(grid), len(grid[0])
        visited = {(0, 0)}
        is_valid = lambda i, j:  0 <= i < n and 0 <= j < m and (new_i, new_j) not in visited
        
        queue = deque([(0, 0)])
        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                if i == n-1 and j == m-1:
                    return True
                for i_drn, j_drn in drn[grid[i][j]]:
                    new_i, new_j = i+i_drn, j+j_drn
                    if is_valid(new_i, new_j) and (-i_drn, -j_drn) in drn[grid[new_i][new_j]]:  # Important BW
                        
                        visited.add((new_i, new_j))
                        queue.append((new_i, new_j))
        return False
                
        
        