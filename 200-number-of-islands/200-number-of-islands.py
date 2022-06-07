class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        dirn_array = [(1, 0),(0, 1),(-1, 0),(0, -1)]
        visited = set()
        is_valid = lambda i, j: 0 <= i < row and 0 <= j < col
        def dfs(i, j):
            visited.add((i, j))
            for i_dir, j_dir in dirn_array:
                new_i, new_j = i+i_dir, j+j_dir
                if is_valid(new_i, new_j) and grid[new_i][new_j] == "1"\
                    and (new_i, new_j) not in visited:
                    dfs(new_i, new_j)
        
        an = 0
        for i in range(row):
            # print(visited)
            for j in range(col):
                if (i, j) not in visited and grid[i][j] == "1":
                    dfs(i, j)
                    an += 1
        return an
            