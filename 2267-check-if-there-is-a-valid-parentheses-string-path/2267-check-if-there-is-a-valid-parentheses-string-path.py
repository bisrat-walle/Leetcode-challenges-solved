class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        if grid[0][0] != "(":
            return False
        n = len(grid)
        m = len(grid[0])
        
        queue = deque([((0, 0), 1)])
        drn = [(0, 1), (1, 0)]
        is_valid = lambda i, j: 0 <= i < n and 0 <= j < m
        possibilities = []
        visited = {((0, 0), 1)}
        while queue:
            for _ in range(len(queue)):
                (i, j), openning = queue.popleft()
                if i == n-1 and j == m-1:
                    if openning == 0:
                        return True
                else:
                    for i_drn, j_drn in drn:
                        new_i, new_j = i+i_drn, j+j_drn
                        if is_valid(new_i, new_j):
                            isClosing = grid[new_i][new_j] == ")"
                            if isClosing and not openning:
                                continue
                            if isClosing:
                                newOpenning = openning-1
                            else:
                                newOpenning = openning+1
                            if ((new_i, new_j),newOpenning) not in visited:
                                visited.add(((new_i, new_j),newOpenning))
                                queue.append(((new_i, new_j), newOpenning))
        return False