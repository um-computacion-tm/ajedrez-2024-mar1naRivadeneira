import unittest
from chess.king import King
from chess.board import Board
from chess.pawn import Pawn

class TestKing(unittest.TestCase):

    def setUp(self):
        self.board = Board(for_test=True)

    def test_str(self):
        king = King("WHITE", self.board)
        self.assertEqual(
            str(king),
            "♔",
        )

    def test_king_one_step_vertical_asc(self):
        king = King("WHITE", self.board)
        possibles = king.get_valid_moves(4, 4, 3, 4)
        self.assertTrue(possibles)

    def test_king_one_step_vertical_desc(self):
        king = King("WHITE", self.board)
        possibles = king.get_valid_moves(4, 4, 5, 4)
        self.assertTrue(possibles)

    def test_king_one_step_horizontal_derecha(self):
        king = King("WHITE", self.board)
        possibles = king.get_valid_moves(4, 4, 4, 5)
        self.assertTrue(possibles)

    def test_king_one_step_horizontal_izquierda(self):
        king = King("WHITE", self.board)
        possibles = king.get_valid_moves(4, 4, 4, 3)
        self.assertTrue(possibles)

    def test_king_one_step_diagonal_asc_derecha(self):
        king = King("WHITE", self.board)
        possibles = king.get_valid_moves(4, 4, 3, 5)
        self.assertTrue(possibles)

    def test_king_one_step_diagonal_asc_izquierda(self):
        king = King("WHITE", self.board)
        possibles = king.get_valid_moves(4, 4, 3, 3)
        self.assertTrue(possibles)

    def test_king_one_step_diagonal_desc_derecha(self):
        king = King("WHITE", self.board)
        possibles = king.get_valid_moves(4, 4, 5, 5)
        self.assertTrue(possibles)

    def test_king_one_step_diagonal_desc_izquierda(self):
        king = King("WHITE", self.board)
        possibles = king.get_valid_moves(4, 4, 5, 3)
        self.assertTrue(possibles)

    def test_king_invalid_move_two_steps_vertical(self):
        king = King("WHITE", self.board)
        possibles = king.get_valid_moves(4, 4, 2, 4)
        self.assertFalse(possibles)

    def test_king_invalid_move_two_steps_horizontal(self):
        king = King("WHITE", self.board)
        possibles = king.get_valid_moves(4, 4, 4, 6)
        self.assertFalse(possibles)

    def test_king_move_with_blocking_own_piece(self):
        self.board.set_piece(3, 3, Pawn("WHITE", self.board))
        king = King("WHITE", self.board)
        self.board.set_piece(4, 4, king)
        possibles = king.get_valid_moves(4, 4, 3, 3)
        self.assertFalse(possibles)

    def test_king_move_with_blocking_opponent_piece(self):
        self.board.set_piece(3, 3, Pawn("BLACK", self.board))
        king = King("WHITE", self.board)
        self.board.set_piece(4, 4, king)
        possibles = king.get_valid_moves(4, 4, 3, 3)
        self.assertTrue(possibles)

if __name__ == '__main__':
    unittest.main()
