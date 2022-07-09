class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        an = [[1]]
        def rec(numRows):
            if numRows == 2:
                an.append([1, 1])
                return [1, 1]
            prev = rec(numRows-1)
            current = [prev[0]]
            for index in range(len(prev)):
                if index == len(prev) - 1:
                    current.append(prev[index])
                else:
                    current.append(prev[index]+prev[index+1])
            an.append(current)
            return current
        rec(numRows)
        return an
            