class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        arr = []
        while columnNumber > 0:
            arr.append(chr(65+(columnNumber-1)%26))
            columnNumber = (columnNumber-1) // 26
        arr.reverse()
        return ''.join(arr)
            