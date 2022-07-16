class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        temp = []
        for row in board:
            temp.append([i for i in row])
        is_valid = lambda i, j: 0 <= i < len(board) and 0 <= j < len(board[0])
        drn = [(0, 1), (1, 0), (-1, 0), (0, -1), (-1, -1), (1, 1), (-1, 1), (1, -1)]
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                live = temp[i][j] == 1
                live_niegh = 0
                for i_drn, j_drn in drn:
                    i_new, j_new = i + i_drn, j + j_drn
                    if is_valid(i_new, j_new):
                        if temp[i_new][j_new] == 1:
                            live_niegh += 1
                # print(i, j, live, live_niegh)
                if live:
                    if live_niegh < 2 or live_niegh > 3:
                        board[i][j] = 0
                        # print(i, j, "died")
                else:
                    if live_niegh == 3:
                        board[i][j] = 1
                        # print(i, j, "live")