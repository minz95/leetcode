class TicTacToe:

    def __init__(self, n: int):
        self.board = [[0] * n for _ in range(n)]

    def valid(self, row: int, col: int):
        player = self.board[row][col]
        rowvalid = True
        colvalid = True
        for i in range(len(self.board)):
            if self.board[i][col] != player:
                colvalid = False
            if self.board[row][i] != player:
                rowvalid = False
        diagvalid = True
        antivalid = True
        for i in range(len(self.board)):
            if self.board[i][i] != player:
                diagvalid = False
            if self.board[i][len(self.board)-i-1] != player:
                antivalid = False
        return player if rowvalid or colvalid or diagvalid or antivalid else 0

    def move(self, row: int, col: int, player: int) -> int:
        self.board[row][col] = player
        return self.valid(row, col)


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)