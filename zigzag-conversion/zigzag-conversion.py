class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        rows = ["" for i in range(numRows)]
        
        direction = -1
        row = 0
        for i in range(len(s)):
            
            rows[row]+=s[i]
            if (row == 0 or row==numRows-1):
                direction *= -1
            row+=direction
            
        return "".join(rows)
                