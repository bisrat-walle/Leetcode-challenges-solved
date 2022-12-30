class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        """
        [
            [1, 1],
            [3, 4]
        ]
        [
            [1, 1],
            [2, 4]
        ]
        [
            [1, 1],
            [2, 4]
        ]
        """
        n, m = len(grid), len(grid[0])
        mod = 10**9 + 7
        
        dp = [[1 for i in range(m)] for j in range(n)]
        
        heap = []
        
        for i in range(n):
            for j in range(m):
                heappush(heap, (grid[i][j], i, j))
        
        dirns = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        is_valid = lambda i, j: 0 <= i < n and 0 <= j < m
        
        while heap:
            val, i, j = heappop(heap)
            for i_drn, j_drn in dirns:
                new_i, new_j = i+i_drn, j+j_drn
                if is_valid(new_i, new_j) and grid[i][j] > grid[new_i][new_j]:
                    dp[i][j] = (dp[i][j] + dp[new_i][new_j]) % mod
        
        ans = 0
        for i in range(n):
            for j in range(m):
                ans = (ans + dp[i][j]) % mod
        
        return ans