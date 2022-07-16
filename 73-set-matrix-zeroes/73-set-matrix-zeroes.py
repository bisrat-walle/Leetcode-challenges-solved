class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        rows, cols = set(), set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        # print(rows, cols)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in rows or j in cols:
                    # print(i, j)
                    matrix[i][j] = 0