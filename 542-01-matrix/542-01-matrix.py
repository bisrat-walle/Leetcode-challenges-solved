class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        drn = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        row, col = len(mat), len(mat[0])
        is_valid = lambda i, j: 0 <= i < row and 0 <= j < col
        visited = set()
        queue = deque()
        an = [[0 for i in range(col)] for j in range(row)]
        for i in range(row):
            for j in range(col):
                if mat[i][j] == 1:
                    an[i][j] = float("inf")
                else:
                    queue.append((i, j))
                    
        while queue:
            for _ in range(len(queue)):
                (i, j) = queue.popleft()
                visited.add((i, j))
                for i_dir, j_dir in drn:
                    new_i, new_j = i+i_dir, j + j_dir
                    if is_valid(new_i, new_j) and an[new_i][new_j] > an[i][j]+1:
                        an[new_i][new_j] = an[i][j]+1
                        queue.append((new_i, new_j))
        
        
        return an