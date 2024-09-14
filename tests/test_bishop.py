import unittest
from chess.bishop import Bishop
from chess.board import Board

class TestBishop(unittest.TestCase):
    
    def test_str(self):
        board = Board()
        bishop = Bishop("WHITE", board)
        self.assertEqual(
            str(bishop),
            "♗",
        )
    
    def test_move_up_izquierda(self):
        board = Board(for_test = True)
        bishop = Bishop("WHITE", board)
        possibles = bishop.possible_positions_dai(3, 3)
        self.assertEqual(
            possibles,
            [(2, 2), (1, 1), (0, 0)]
        )
    
if __name__ == '__main__':
    unittest.main()       