import unittest
from chess.board import Board
from chess.rook import Rook
from chess.queen import Queen
from chess.bishop import Bishop
from chess.knight import Knight 
from chess.pawn import Pawn 
from chess.king import King
from chess.excepciones import OutOfBoard

class TestBoard(unittest.TestCase):  #verifica la representacion del tablero y las piezas 
    
    def setUp(self):
        self.board = Board()
        
    def test_str_board(self):
        board = Board()
        self.assertEqual(
            str(board),
            (
                "  0 1 2 3 4 5 6 7\n"
                "0 ♜ ♞ ♝ ♛ ♚ ♝ ♞ ♜ 0\n"
                "1 ♟ ♟ ♟ ♟ ♟ ♟ ♟ ♟ 1\n"
                "2 . . . . . . . . 2\n"
                "3 . . . . . . . . 3\n"
                "4 . . . . . . . . 4\n"
                "5 . . . . . . . . 5\n"
                "6 ♙ ♙ ♙ ♙ ♙ ♙ ♙ ♙ 6\n"
                "7 ♖ ♘ ♗ ♕ ♔ ♗ ♘ ♖ 7\n"
                "  0 1 2 3 4 5 6 7"
            )
        )
        
    def test_move(self):
        board = Board(for_test=True)
        rook = Rook(color='BLACK', board=board)
        board.set_piece(0, 0, rook)
        
        board.move(
            from_row=0,
            from_col=0,
            to_row=2,
            to_col=0,
        )
        
        self.assertIsInstance(
            board.get_piece(2, 0),
            Rook,
        )
        
        self.assertEqual(
            str(board),
            (
                "  0 1 2 3 4 5 6 7\n"
                "0 . . . . . . . . 0\n"
                "1 . . . . . . . . 1\n"
                "2 ♜ . . . . . . . 2\n"
                "3 . . . . . . . . 3\n"
                "4 . . . . . . . . 4\n"
                "5 . . . . . . . . 5\n"
                "6 . . . . . . . . 6\n"
                "7 . . . . . . . . 7\n"
                "  0 1 2 3 4 5 6 7"
            )
        )
 
    def test_get_piece_out_of_range(self):
        board = Board(for_test=True)
        
        with self.assertRaises(OutOfBoard) as exc:
            board.get_piece(10, 10)

        self.assertEqual(
            exc.exception.message,
            "La posicion indicada se encuentra fuera del tablero"
        )
        
    def test_posiciones_iniciales_de_piezas(self):
        
        self.assertIsInstance(self.board.get_piece(0, 3), Queen)    
        self.assertIsInstance(self.board.get_piece(7, 3), Queen)
        
        self.assertIsInstance(self.board.get_piece(0, 2), Bishop)
        self.assertIsInstance(self.board.get_piece(7, 5), Bishop)
        
        self.assertIsInstance(self.board.get_piece(0, 0), Rook)
        self.assertIsInstance(self.board.get_piece(7, 7), Rook)
        
        
if __name__ == '__main__':
    unittest.main()        