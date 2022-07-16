class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        drn = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        @lru_cache(None)
        def solve(moves, i, j):
            if (i == m or j == n or i < 0 or j < 0):
                return 1
            if (moves == 0): 
                return 0
            an = 0
            for i_drn, j_drn in drn:
                an += solve(moves-1, i + i_drn, j + j_drn)
            return an
        
        return solve(maxMove, startRow, startColumn) % (10**9 + 7)
