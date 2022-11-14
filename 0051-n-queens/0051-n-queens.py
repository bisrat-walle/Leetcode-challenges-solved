class Solution:
    def isSafe(self, r, c, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(n):
                if r == i or c == j or r+c == i+j or r-c == i-j:
                    if matrix[i][j] == "Q":
                        return False
        return True

    def solve(self, r, matrix, ans):
        n = len(matrix)
        if r == n:
            ans.append(["".join(row) for row in matrix])
            return
        for i in range(n):
            if self.isSafe(r, i, matrix):
                matrix[r][i] = "Q"  # place the queen
                self.solve(r+1, matrix, ans)
                matrix[r][i] = "."  # backtrack (remove the queen)
                
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        matrix = [["." for i in range(n)] for j in range(n)]
        self.solve(0, matrix, ans)
        return ans