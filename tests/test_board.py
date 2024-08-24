import unittest
from chess.board import Board
from chess.rook import Rook
from chess.queen import Queen
from chess.bishop import Bishop

class TestBoard(unittest.TestCase):  #verifica la representacion del tablero
    def test_str_board(self):
        board = Board()
        self.assertEqual(
            str(board),
            (
                "♖      ♖\n"
                "        \n"
                "        \n"
                "        \n"
                "        \n"
                "        \n"
                "        \n"
                "♜      ♜\n"
            )
        )
    
    def setUp(self):
        self.board = Board()
        
    def test_posiciones_iniciales_de_piezas(self):
        
        self.assertIsInstance(self.board.get_piece(0, 3), Queen)    
        self.assertIsInstance(self.board.get_piece(7, 3), Queen)
        
        self.assertIsInstance(self.board.get_piece(0, 2), Bishop)
        self.assertIsInstance(self.board.get_piece(7, 5), Bishop)
        
        self.assertIsInstance(self.board.get_piece(0, 0), Rook)
        self.assertIsInstance(self.board.get_piece(7, 7), Rook)
        
        
if __name__ == '__main__':
    unittest.main()        