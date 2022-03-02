class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        def dfs(i, j):
            if (i, j) in visited:
                return
            if board[i][j] == "O":
                visited.add((i, j))
                if i >= 1:
                    dfs(i-1, j)
                if i < len(board)-1:
                    dfs(i+1, j)
                if j >= 1:
                    dfs(i, j-1)
                if j < len(board[0])-1:
                    dfs(i, j+1)
        
        visited = set()
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    if i == 0 or i == len(board)-1 or j == 0 or j == len(board[0])-1:
                        if (i,j) not in visited:
                            dfs(i, j)
        # print(visited)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O" and (i, j) not in visited:
                    board[i][j] = "X"
        