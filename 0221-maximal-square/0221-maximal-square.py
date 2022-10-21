class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n, m = len(matrix), len(matrix[0])
        dp = [[int(matrix[i][j] == "1") for j in range(m)] for i in range(n)]
        
        for i in range(1, n):
            for j in range(1, m):
                if dp[i][j] == 1:
                    dp[i][j] += min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])
        # print(dp)
        return (max(max(i) for i in dp))**2