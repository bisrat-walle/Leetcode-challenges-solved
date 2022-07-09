class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        def rec(rowIndex):
            if rowIndex == 2:
                return [1, 1]
            prev = rec(rowIndex-1)
            current = [prev[0]]
            for index in range(len(prev)):
                if index == len(prev) - 1:
                    current.append(prev[index])
                else:
                    current.append(prev[index]+prev[index+1])
            return current
        return rec(rowIndex+1)