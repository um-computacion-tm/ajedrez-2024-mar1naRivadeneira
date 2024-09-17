import unittest
from chess.bishop import Bishop
from chess.board import Board

class TestBishop(unittest.TestCase):
    def setUp(self):
        self.board = Board(for_test = True)
    
    def test_str(self):
        board = Board()
        bishop = Bishop("WHITE", board)
        self.assertEqual(
            str(bishop),
            "♗",
        )
    
    def test_move_diagonal_asc_izquierda(self):
        bishop = Bishop("WHITE", self.board)
        possibles = bishop.possible_positions_dai(3, 3)
        self.assertEqual(
            possibles,
            [(2, 2), (1, 1), (0, 0)]
        )
     
    def test_move_diagonal_asc_derecha(self):
        bishop = Bishop("WHITE", self.board)
        possibles = bishop.possible_positions_dad(4, 4)
        self.assertEqual(
            possibles,
            [(3, 5), (2, 6), (1, 7)]    
        )
        
    def test_move_diagonal_desc_izquierda(self):
        bishop = Bishop("WHITE", self.board)
        possibles = bishop.possible_positions_ddi(4, 4)
        self.assertEqual(
            possibles,
            [(5, 3), (6, 2), (7, 1)]
        )
        
    def test_move_diagonal_desc_derecha(self):
        bishop = Bishop("WHITE", self.board)
        possibles = bishop.possible_positions_ddd(4, 4)
        self.assertEqual(
            possibles,
            [(5, 5), (6, 6), (7, 7)]
        )
        
    
if __name__ == '__main__':
    unittest.main()       