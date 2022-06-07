class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        is_valid = lambda i, j: 0 <= i < row and 0 <= j < col
        dirn = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        queue = deque()
        visited = set()
        def dfs(i, j):
            grid[i][j] = "*"
            queue.append((i, j))
            for i_dir, j_dir in dirn:
                new_i, new_j = i+i_dir, j+j_dir
                if is_valid(new_i, new_j) and grid[new_i][new_j] == 1 and \
                    (new_i, new_j) not in visited:
                    dfs(new_i, new_j)
            
            
        
        for i in range(row):
            br = False
            for j in range(col):
                if grid[i][j] == 1:
                    dfs(i, j)
                    br = True
                    break
            if br: break
        
        an = 0
        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for i_dir, j_dir in dirn:
                    new_i, new_j = i+i_dir, j+j_dir
                    if is_valid(new_i, new_j) and  (new_i, new_j) not in visited:
                        if grid[new_i][new_j] == 1:
                            return an
                        elif grid[new_i][new_j] == 0:
                            grid[new_i][new_j] = "*"
                            queue.append((new_i, new_j))
            an += 1
        
            
        # return an
            