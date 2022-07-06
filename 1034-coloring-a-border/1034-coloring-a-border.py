class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        old_color = grid[row][col]
        visited = {(row, col)}
        drn_array = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        is_valid = lambda i, j: 0 <= i < len(grid) and 0 <= j < len(grid[0])
        def dfs(i, j):
            for i_dr, j_dr in drn_array:
                new_i, new_j = i+i_dr, j+j_dr
                # print((new_i, new_j), visited)
                if is_valid(new_i, new_j) and (new_i, new_j) not in visited and \
                        grid[new_i][new_j] == old_color:
                    visited.add((new_i, new_j))
                    # print((new_i, new_j),"Valid and not visited")
                    dfs(new_i, new_j)
            
        dfs(row, col)
        # print(visited)
        for i, j in visited:
            is_boundary = False
            for i_dr, j_dr in drn_array:
                new_i, new_j = i+i_dr, j+j_dr
                if (not is_valid(new_i, new_j)) or (new_i, new_j) not in visited:
                    is_boundary = True
                    break
            if is_boundary:
                grid[i][j] = color
        
        return grid