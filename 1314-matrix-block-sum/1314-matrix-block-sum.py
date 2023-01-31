class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        """
        45 0 0 1
        [
            [1, 3, 6], 
            [5, 12, 21], 
            [12, 27, 45]
        ]

        """
        m, n = len(mat), len(mat[0])
        prefix = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                prefix[i][j] += mat[i][j]
                if j != 0:
                    prefix[i][j] += prefix[i][j-1]
        
        
        for i in range(m):
            for j in range(n):
                if i != 0:
                    prefix[i][j] += prefix[i-1][j]
                    
        
        is_valid = lambda i, j: 0 <= i < m and 0 <= j < n
        
        
        ans = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                r, c = min(m-1, i+k), min(n-1, j+k)
                large_rectangle_sum = prefix[r][c]
                r, c = i-k-1, min(j+k, n-1)
                top_rectangle_sum = prefix[r][c] if is_valid(r, c) else 0
                r, c = min(i+k, m-1), j-k-1
                left_rectangle_sum = prefix[r][c] if is_valid(r, c) else 0
                r, c = i-k-1, j-k-1
                twice_deducted_rectangle_sum = prefix[r][c] if is_valid(r, c) else 0
                ans[i][j] = large_rectangle_sum - top_rectangle_sum - \
                                left_rectangle_sum + twice_deducted_rectangle_sum
                
        return ans
        