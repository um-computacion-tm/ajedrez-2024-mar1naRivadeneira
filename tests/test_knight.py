import unittest
from chess.knight import Knight
from chess.board import Board
from  chess.pawn import Pawn

class TestKnight(unittest.TestCase):

    def setUp(self):
        self.board = Board(for_test=True)

    def test_str(self):
        knight = Knight("WHITE", self.board)
        self.assertEqual(
            str(knight),
            "♘",
        )

    def test_valid_move_L_shape_up_right(self):
        knight = Knight("WHITE", self.board)
        possibles = knight.get_valid_moves(4, 4)
        self.assertIn((2, 5), possibles)

    def test_valid_move_L_shape_up_left(self):
        knight = Knight("WHITE", self.board)
        possibles = knight.get_valid_moves(4, 4)
        self.assertIn((2, 3), possibles)

    def test_valid_move_L_shape_down_right(self):
        knight = Knight("WHITE", self.board)
        possibles = knight.get_valid_moves(4, 4)
        self.assertIn((6, 5), possibles)

    def test_valid_move_L_shape_down_left(self):
        knight = Knight("WHITE", self.board)
        possibles = knight.get_valid_moves(4, 4)
        self.assertIn((6, 3), possibles)

    def test_valid_move_L_shape_right_up(self):
        knight = Knight("WHITE", self.board)
        possibles = knight.get_valid_moves(4, 4)
        self.assertIn((3, 6), possibles)

    def test_valid_move_L_shape_right_down(self):
        knight = Knight("WHITE", self.board)
        possibles = knight.get_valid_moves(4, 4)
        self.assertIn((5, 6), possibles)

    def test_valid_move_L_shape_left_up(self):
        knight = Knight("WHITE", self.board)
        possibles = knight.get_valid_moves(4, 4)
        self.assertIn((3, 2), possibles)

    def test_valid_move_L_shape_left_down(self):
        knight = Knight("WHITE", self.board)
        possibles = knight.get_valid_moves(4, 4)
        self.assertIn((5, 2), possibles)

    def test_invalid_move_straight(self):
        knight = Knight("WHITE", self.board)
        possibles = knight.get_valid_moves(4, 4)
        self.assertNotIn((4, 6), possibles)

    def test_invalid_move_diagonal(self):
        knight = Knight("WHITE", self.board)
        possibles = knight.get_valid_moves(4, 4)
        self.assertNotIn((6, 6), possibles)

    def test_move_with_blocking_own_piece(self):
        self.board.set_piece(2, 5, Pawn("WHITE", self.board))
        knight = Knight("WHITE", self.board)
        possibles = knight.get_valid_moves(4, 4)
        self.assertNotIn((2, 5), possibles)

    def test_move_with_blocking_opponent_piece(self):
        self.board.set_piece(2, 5, Pawn("BLACK", self.board))
        knight = Knight("WHITE", self.board)
        possibles = knight.get_valid_moves(4, 4)
        self.assertIn((2, 5), possibles)

if __name__ == '__main__':
    unittest.main()
