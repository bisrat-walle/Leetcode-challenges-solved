class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        n = len(grid)
        queue = deque([[(0, 0), (0, 1), 0]])
        visited = {((0, 0), (0, 1))}
        directions = [[(0, 1), (0, 1)], 
                      [(1, 0), (1, 0)], 
                      [(0, 0), (1, -1)], 
                      [(0, 0), (-1, 1)]]

        def validate(i1, j1, i2, j2, index):
            if not (0 <= i1 < n and 0 <= j1 < n and 0 <= i2 < n and 0 <= j2 < n):
                return False
            
            if grid[i1][j1] != 0 or grid[i2][j2] != 0:
                return False
            
            if index >= 2:  # Edge Case 1
                if grid[i1+1][j1+1] == 1:
                    return False
            
            return True

        
        while queue:
            
            c1, c2, step = queue.popleft()
            i1, j1 = c1
            i2, j2 = c2

            if i1 == n-1 and j1 == n-2 and i2 == n-1 and j2 == n-1:
                return step

            for index in range(len(directions)):
                if index == 2:
                    if i1 != i2:
                        continue
                if index == 3:
                    if j1 != j2:
                        continue
                c1_drn, c2_drn = directions[index]
                i1_drn, j1_drn = c1_drn
                i2_drn, j2_drn = c2_drn

                new_i1 = i1+i1_drn
                new_j1 = j1+j1_drn

                new_i2 = i2+i2_drn
                new_j2 = j2+j2_drn
                if validate(new_i1, new_j1, new_i2, new_j2, index) and ((new_i1, new_j1), (new_i2, new_j2)) not in visited:
                    visited.add(((new_i1, new_j1), (new_i2, new_j2)))
                    # print(step, ((new_i1, new_j1), (new_i2, new_j2), step+1))
                    queue.append(((new_i1, new_j1), (new_i2, new_j2), step+1))

        return -1