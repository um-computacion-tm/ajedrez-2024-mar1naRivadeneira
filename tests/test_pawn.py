import unittest
from chess.board import Board
from chess.pawn import Pawn
from chess.queen import Queen

class TestPawn(unittest.TestCase):

    def setUp(self):
        self.board = Board(for_test=True)  
    
    '''def test_white_pawn_single_move(self):
        pawn = Pawn("WHITE", self.board)
        self.board.set_piece(6, 4, pawn)  
        moves = pawn.possible_moves(6, 4)
        
        # El peón blanco debe poder moverse a (5, 4)
        self.assertIn((5, 4), moves)
        self.assertNotIn((4, 4), moves)'''  # No puede moverse dos casillas si ya ha avanzado

    def test_white_pawn_double_move(self):
        pawn = Pawn("WHITE", self.board)
        self.board.set_piece(6, 4, pawn)
        
        moves = pawn.possible_moves(6, 4)
        
        # El peón blanco en su primera jugada puede moverse a (5, 4) o (4, 4)
        self.assertIn((5, 4), moves)
        self.assertIn((4, 4), moves)

    '''def test_black_pawn_single_move(self):
        pawn = Pawn("BLACK", self.board)
        self.board.set_piece(1, 4, pawn)
        
        moves = pawn.possible_moves(1, 4)
        
        # El peón negro debe poder moverse a (2, 4)
        self.assertIn((2, 4), moves)
        self.assertNotIn((3, 4), moves)'''  # No puede avanzar dos casillas después de mover

    def test_black_pawn_double_move(self):
        pawn = Pawn("BLACK", self.board)
        self.board.set_piece(1, 4, pawn)
        
        moves = pawn.possible_moves(1, 4)
        
        # El peón negro en su primera jugada puede moverse a (2, 4) o (3, 4)
        self.assertIn((2, 4), moves)
        self.assertIn((3, 4), moves)

    def test_pawn_diagonal_capture(self):
        white_pawn = Pawn("WHITE", self.board)
        black_pawn = Pawn("BLACK", self.board)
        self.board.set_piece(6, 4, white_pawn)
        self.board.set_piece(5, 3, black_pawn)
        
        moves = white_pawn.possible_moves(6, 4)
        
        # El peón blanco debería poder capturar en diagonal hacia (5, 3)
        self.assertIn((5, 3), moves)

    def test_pawn_promotion(self):
        # Colocamos un peón blanco listo para ser promovido
        pawn = Pawn("WHITE", self.board)
        self.board.set_piece(1, 4, pawn)
        
        moves = pawn.possible_moves(1, 4)
        
        # Movemos el peón a la última fila
        pawn.promote(0, 4)
        
        # Verificamos si el peón fue promovido a reina
        piece = self.board.get_piece(0, 4)
        self.assertIsInstance(piece, Queen)

    def test_pawn_blocked_move(self):
        white_pawn = Pawn("WHITE", self.board)
        blocking_pawn = Pawn("WHITE", self.board)
        self.board.set_piece(6, 4, white_pawn)
        self.board.set_piece(5, 4, blocking_pawn)
        
        moves = white_pawn.possible_moves(6, 4)
        
        # El peón no debería poder moverse si está bloqueado
        self.assertNotIn((5, 4), moves)

if __name__ == '__main__':
    unittest.main()
