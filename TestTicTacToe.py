import unittest
from TicTacToe import TicTacToe


class TestTicTacToe(unittest.TestCase):

    def testActiveFieldsIsNine(self):
        game = TicTacToe()
        result = 0
        for i in range(len(game.board)):
            for j in range(len(game.board[i])):
                result = result + 1
        self.assertEqual(result, 9)

    def testCurrentPlayerIsX(self):
        game = TicTacToe()
        if game.currentPlayer() == 'X':
            result = True
        else:
            result = False
        self.assertEqual(result, True)

    def testCurrentPlayerIsO(self):
        game = TicTacToe()
        game.changePlayer()
        if game.currentPlayer() == 'O':
            result = True
        else:
            result = False
        self.assertEqual(result, True)

    def testCurrentPlayerPlacesX(self):
        game = TicTacToe()
        game.currentplayer = 'X'
        game.makeMove(0, 0)
        assert (game.board[0][0] == 'X')

    def testCurrentPlayerPlacesO(self):
        game = TicTacToe()
        game.currentplayer = 'O'
        game.makeMove(0, 0)
        assert (game.board[0][0] == 'O')

    def testUnoccupiedPlacement(self):
        game = TicTacToe()
        assert(game.board[0][0] == '')
        game.makeMove(0, 0)
        assert(game.board[0][0] == 'X')
        assert(game.makeMove(0, 0) == False)


if __name__ == '__main__':
    unittest.main()
