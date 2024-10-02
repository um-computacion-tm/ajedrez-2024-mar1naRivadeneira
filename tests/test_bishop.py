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
        possibles = bishop.valid_positions(3, 3, 0, 0)
        self.assertTrue(possibles)
     
    def test_move_diagonal_asc_derecha(self):
        bishop = Bishop("WHITE", self.board)
        possibles = bishop.valid_positions(4, 4, 2, 6)
        self.assertTrue(possibles)
        
    def test_move_diagonal_desc_izquierda(self):
        bishop = Bishop("WHITE", self.board)
        possibles = bishop.valid_positions(4, 4, 7, 1)
        self.assertTrue(possibles)
        
    def test_move_diagonal_desc_derecha(self):
        bishop = Bishop("WHITE", self.board)
        possibles = bishop.valid_positions(4, 4, 6, 6)
        self.assertTrue( possibles,)
        
    def test_move_diagonal_asc_izquierda_with_own_piece(self):
        self.board.set_piece(2, 2, Bishop("WHITE", self.board))
        bishop = Bishop("WHITE", self.board)
        self.board.set_piece(5, 5, bishop)
        possibles = bishop.valid_positions(5, 5, 3, 3)
        self.assertTrue(possibles) 
        
    def test_move_diagonal_asc_izquierda_with_opponent_piece(self):
        self.board.set_piece(3, 3, Bishop("BLACK", self.board))
        bishop = Bishop("WHITE", self.board)
        self.board.set_piece(4, 4, bishop)
        possibles = bishop.valid_positions(4, 4, 3, 3)
        self.assertTrue(possibles)               
     
    def test_move_diagonal_asc_derecha_with_own_piece(self):
        self.board.set_piece(3, 5, Bishop("WHITE", self.board))
        bishop = Bishop("WHITE", self.board)
        self.board.set_piece(4, 4, bishop)
        possibles = bishop.valid_positions(4, 4, 5, 5)                      
        self.assertTrue(possibles)
        
    def test_move_diagonal_asc_derecha_with_opponent_piece(self):
        self.board.set_piece(3, 5, Bishop("BLACK", self.board))
        bishop = Bishop("WHITE", self.board)
        self.board.set_piece(4, 4, bishop)
        possibles = bishop.valid_positions(4, 4, 3, 5)
        self.assertTrue(possibles)  
        
    def test_move_diagonal_desc_izquierda_with_own_piece(self):
        self.board.set_piece(6, 2, Bishop("WHITE", self.board))
        bishop = Bishop("WHITE", self.board)
        self.board.set_piece(4, 4, bishop)
        possibles = bishop.valid_positions(4, 4, 5, 3)
        self.assertTrue(possibles)
        
    def test_move_diagonal_desc_derecha_with_opponent_piece(self):
        self.board.set_piece(6, 6, Bishop("BLACK", self.board))
        bishop = Bishop("WHITE", self.board)
        self.board.set_piece(4, 4, bishop)
        possibles = bishop.valid_positions(4, 4, 6, 6)
        self.assertTrue(possibles)
          
if __name__ == '__main__':
    unittest.main()       