class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        for i in matrix:
            if len(i) != len(set(i)):
                return False
        
        for j in range(n):
            temp = set()
            for i in range(n):
                if matrix[i][j] in temp:
                    return False
                temp.add(matrix[i][j])
        
        return True
            