class TicTacToe:
    def __init__(self):
        self.board = self.createBoard()
        self.currentplayer = 'X'

    def createBoard(self):
        board = (['','',''],['','',''],['','',''])
        return board

    def currentPlayer(self):
        return self.currentplayer

    def changePlayer(self):
        global currentplayer
        if self.currentPlayer() == 'X':
            self.currentplayer = 'O'
        elif self.currentPlayer() == 'O':
            self.currentplayer = 'X'

    def makeMove(self, row, col):
        if self.currentplayer == 'X' and self.board[row][col] == "" and self.board[row][col] != 'X' and self.board[row][col] != 'O':
            self.board[row][col] = 'X'
            self.changePlayer()
            return True
        if self.currentplayer == 'O' and self.board[row][col] == "" and self.board[row][col] != 'X' and self.board[row][col] != 'O':
            self.board[row][col] = 'O'
            self.changePlayer()
            return True
        else:
            return False

    def spaceInUse(self):
        spaceused = 0
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == 'O' or self.board[i][j] == 'X':
                    spaceused = spaceused + 1
        return spaceused

    def play(self):
        game = TicTacToe()
        game.createBoard()
        print(game.board[0])
        print(game.board[1])
        print(game.board[2])

        for i in range(len(game.board)):
            for j in range(len(game.board[i])):
                game.makeMove(i, j)
                print(game.board[0])
                print(game.board[1])
                print(game.board[2])
                print("Space in use " + str(game.spaceInUse()))


if __name__ == '__main__':
    game = TicTacToe()
    game.play()
