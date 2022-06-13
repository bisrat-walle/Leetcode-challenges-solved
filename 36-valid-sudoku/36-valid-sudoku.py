class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        i =  0
        while i < len(board):
            temp1, temp2, temp3 = set(), set(), set()
            for _ in range(3):
                for j in range(len(board[0])):
                    if j < 3:
                        if board[i][j] == ".":
                            continue
                        if board[i][j] in temp1:
                            return False
                        temp1.add(board[i][j])
                    elif j < 6:
                        if board[i][j] == ".":
                            continue
                        if board[i][j] in temp2:
                            return False
                        temp2.add(board[i][j])
                    else:
                        if board[i][j] == ".":
                            continue
                        if board[i][j] in temp3:
                            return False
                        temp3.add(board[i][j])
                i += 1
        
        for i in range(len(board)):
            temp = set()
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    continue
                if board[i][j] in temp:
                    return False
                temp.add(board[i][j])
        
        for j in range(len(board[0])):
            temp = set()
            for i in range(len(board)):
                if board[i][j] == ".":
                    continue
                if board[i][j] in temp:
                    return False
                temp.add(board[i][j])
        
        return True
            