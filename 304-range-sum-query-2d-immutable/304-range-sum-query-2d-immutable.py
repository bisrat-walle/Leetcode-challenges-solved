class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.obj = matrix
        self.dp = None;
        self.NumMatrix(self.obj)
        
    

    def NumMatrix(self, matrix):
        if (len(matrix) == 0 or len(matrix[0]) == 0): return
        self.dp = [[0 for i in range(len(matrix[0])+1)] for i in range(len(matrix))];
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                self.dp[r][c + 1] = self.dp[r][c] + matrix[r][c];
            
        

    

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        s = 0;
        for row in range(row1, row2+1):
            s += self.dp[row][col2 + 1] - self.dp[row][col1];
        
        return s


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)