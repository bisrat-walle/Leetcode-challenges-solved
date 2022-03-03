
class Solution:
    
    def __init__(self):
        self.c = 0
    
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        return self.dfs(image, sr, sc, image[sr][sc], newColor)
        
    
    def dfs(self, image, r, c, color, newColor):
        self.c += 1
        # if self.c == 999:
        #     print(image)
        #     print(r, c)
        # # print(r, c)
        
        if image[r][c] == newColor:
            return image
        
        if image[r][c] == color:
            image[r][c] = newColor
        
            max_row, max_column = len(image), len(image[0])
            if r >= 1:
                self.dfs(image, r-1, c, color, newColor)
            if r < max_row - 1:
                self.dfs(image, r+1, c, color, newColor)
            if c >= 1:
                self.dfs(image, r, c-1, color, newColor)
            if c < max_column - 1:
                self.dfs(image, r, c+1, color, newColor)

        return image