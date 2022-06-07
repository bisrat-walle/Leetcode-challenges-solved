class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row_l, col_l = len(matrix), len(matrix[0])
        discovered = set()
        i_start, i_end, j_start, j_end = 0, row_l, 0, col_l
        an = []
        while i_start < i_end and j_start < j_end :
            # print(i_start, i_end, j_start, j_end)
            for i in range(j_start, j_end):
                an.append(matrix[i_start][i])
            i_start += 1
            
            for i in range(i_start, i_end):
                an.append(matrix[i][j_end-1])
            j_end -= 1
            
            
            if i_start >= i_end or j_start >= j_end:
                break
            
            for i in reversed(range(j_start, j_end)):
                an.append(matrix[i_end-1][i])
                
            i_end -= 1
            
            for i in reversed(range(i_start, i_end)):
                an.append(matrix[i][j_start])
            j_start += 1
            # print(i_start, i_end, j_start, j_end, an, end="\n\n")
        return an