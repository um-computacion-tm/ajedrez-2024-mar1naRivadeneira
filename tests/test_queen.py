import unittest
from chess.queen import Queen 
from chess.board import Board
from chess.pawn import Pawn

class TestQueen(unittest.TestCase):

    def setUp(self):
        self.board = Board(for_test=True)

    def test_str(self):
        queen = Queen("WHITE", self.board)
        self.assertEqual(
            str(queen),
            "♕",
        )

    def test_move_queen_vertical_asc(self):
        queen = Queen("WHITE", self.board)
        possibles = queen.get_valid_moves(4, 1, 2, 1)
        self.assertTrue(possibles)

    def test_move_queen_vertical_desc(self):
        queen = Queen("WHITE", self.board)
        possibles = queen.get_valid_moves(4, 1, 6, 1)
        self.assertTrue(possibles)

    def test_move_queen_horizontal_derecha(self):
        queen = Queen("WHITE", self.board)
        possibles = queen.get_valid_moves(4, 4, 4, 7)
        self.assertTrue(possibles)

    def test_move_queen_horizontal_izquierda(self):
        queen = Queen("WHITE", self.board)
        possibles = queen.get_valid_moves(4, 4, 4, 0)
        self.assertTrue(possibles)

    def test_move_queen_diagonal_asc_derecha(self):
        queen = Queen("WHITE", self.board)
        possibles = queen.get_valid_moves(4, 4, 2, 6)
        self.assertTrue(possibles)

    def test_move_queen_diagonal_asc_izquierda(self):
        queen = Queen("WHITE", self.board)
        possibles = queen.get_valid_moves(4, 4, 2, 2)
        self.assertTrue(possibles)

    def test_move_queen_diagonal_desc_derecha(self):
        queen = Queen("WHITE", self.board)
        possibles = queen.get_valid_moves(4, 4, 6, 6)
        self.assertTrue(possibles)

    def test_move_queen_diagonal_desc_izquierda(self):
        queen = Queen("WHITE", self.board)
        possibles = queen.get_valid_moves(4, 4, 6, 2)
        self.assertTrue(possibles)

    def test_move_queen_with_blocking_own_piece(self):
        self.board.set_piece(5, 5, Pawn("WHITE", self.board))
        queen = Queen("WHITE", self.board)
        self.board.set_piece(4, 4, queen)
        possibles = queen.get_valid_moves(4, 4, 6, 6)
        self.assertFalse(possibles)

    def test_move_queen_with_blocking_opponent_piece(self):
        self.board.set_piece(6, 6, Pawn("BLACK", self.board))
        queen = Queen("WHITE", self.board)
        self.board.set_piece(4, 4, queen)
        possibles = queen.get_valid_moves(4, 4, 6, 6)
        self.assertTrue(possibles)

if __name__ == '__main__':
    unittest.main()
