class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        mapping = defaultdict(set)
        n, m = len(matrix), len(matrix[0])
        for i in range(n):
            for j in range(m):
                mapping[i-j].add(matrix[i][j])
                if len(mapping[i-j]) > 1:
                    return False
        
        return True