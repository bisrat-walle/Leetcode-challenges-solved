class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        queue = deque([tuple(entrance)])
        row, col = len(maze), len(maze[0])
        dirn = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        is_valid = lambda i, j: 0 <= i < row and 0 <= j < col
        is_border = lambda i, j: i in (0, row-1) or j in (0, col-1)
        an = 0
        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                maze[i][j] = "+"
                for i_dir, j_dir in dirn:
                    new_i, new_j = i+i_dir, j+j_dir
                    # print("current", new_i, new_j )
                    if is_valid(new_i, new_j) and maze[new_i][new_j] == ".":
                        # print(new_i,new_j, maze[new_i][new_j])
                        if is_border(new_i, new_j):
                            return an+1
                        maze[new_i][new_j] = "+"
                        queue.append((new_i, new_j))
                
            an += 1
        
        return -1
        