class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        an = 0
        
        for i in range(n):
            for j in range(n):
                if i+j == n-1:
                    an += mat[i][j]
                if i-j == 0:
                    an += mat[i][j]
        return an if n%2 == 0 else an - mat[n//2][n//2]