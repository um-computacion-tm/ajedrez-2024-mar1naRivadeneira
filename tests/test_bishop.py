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
        
    def test_move_diagonal_asc_izquierda_with_own_piece(self):
        self.board.set_piece(3, 3, Bishop("WHITE", self.board))
        bishop = Bishop("WHITE", self.board)
        self.board.set_piece(4, 4, bishop)
        possibles = bishop.possible_positions_dai(4, 4)
        self.assertEqual(
            possibles,
            []
        ) 
        
    def test_move_diagonal_asc_izquierda_with_opponent_piece(self):
        self.board.set_piece(3, 3, Bishop("BLACK", self.board))
        bishop = Bishop("WHITE", self.board)
        self.board.set_piece(4, 4, bishop)
        possibles = bishop.possible_positions_dai(4, 4)
        self.assertEqual(
            possibles,
            [(3, 3)]
        )               
     
    def test_move_diagonal_asc_derecha_with_own_piece(self):
        self.board.set_piece(3, 5, Bishop("WHITE", self.board))
        bishop = Bishop("WHITE", self.board)
        self.board.set_piece(4, 4, bishop)
        possibles = bishop.possible_positions_dad(4, 4)
        self.assertEqual(
            possibles,
            []
        )
        
    def test_move_diagonal_asc_derecha_with_opponent_piece(self):
        self.board.set_piece(3, 5, Bishop("BLACK", self.board))
        bishop = Bishop("WHITE", self.board)
        self.board.set_piece(4, 4, bishop)
        possibles = bishop.possible_positions_dad(4, 4)
        self.assertEqual(
            possibles,
            [(3, 5)]
        )  
        
    def test_move_diagonal_desc_izquierda_with_own_piece(self):
        self.board.set_piece(6, 2, Bishop("WHITE", self.board))
        bishop = Bishop("WHITE", self.board)
        self.board.set_piece(4, 4, bishop)
        possibles = bishop.possible_positions_ddi(4, 4)
        self.assertEqual(
            possibles,
            [(5, 3)]
        )
        
    def test_move_diagonal_desc_derecha_with_opponent_piece(self):
        self.board.set_piece(6, 6, Bishop("BLACK", self.board))
        bishop = Bishop("WHITE", self.board)
        self.board.set_piece(4, 4, bishop)
        possibles = bishop.possible_positions_ddd(4, 4)
        self.assertEqual(
            possibles,
            [(5, 5), (6, 6)]
        )
          
if __name__ == '__main__':
    unittest.main()       