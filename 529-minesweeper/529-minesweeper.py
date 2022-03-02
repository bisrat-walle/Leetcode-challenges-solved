class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        
        def no_of_adjecent_mine(i, j):
            mines = 0
            if i >= 1 and board[i-1][j] == "M":
                mines += 1
            if i < len(board)-1 and board[i+1][j] == "M":
                mines += 1
            if j >= 1 and board[i][j-1] == "M":
                mines += 1
            if j < len(board[0])-1 and board[i][j+1] == "M":
                mines += 1
            if i >= 1 and j >= 1 and board[i-1][j-1] == "M":
                mines += 1
            if i >= 1 and j < len(board[0])-1 and board[i-1][j+1] == "M":
                mines += 1
            if j >= 1 and i < len(board)-1 and board[i+1][j-1] == "M":
                mines += 1
            if i < len(board)-1 and j < len(board[0])-1 and board[i+1][j+1] == "M":
                mines += 1
            return mines
        
        def reveal(i, j):
            if board[i][j] == "M":
                board[i][j]= "X"
            if board[i][j] == "E":
                ad_mines = no_of_adjecent_mine(i, j)
                if ad_mines == 0:
                    board[i][j] = "B"
                    if i >= 1:
                        reveal(i-1, j)
                    if i < len(board)-1:
                        reveal(i+1, j)
                    if j >= 1:
                        reveal(i, j-1)
                    if j < len(board[0])-1:
                        reveal(i, j+1)
                    
                    if i >= 1 and j >= 1:
                        reveal(i-1, j-1)
                    if i >= 1 and j < len(board[0])-1:
                        reveal(i-1, j+1)
                    if j >= 1 and i < len(board)-1:
                        reveal(i+1, j-1)
                    if i < len(board)-1 and j < len(board[0])-1:
                        reveal(i+1, j+1)
                else:
                    board[i][j] = str(ad_mines)
            # if board[i][j] == ""
                
                
        
        reveal(click[0], click[1])
        
        return board