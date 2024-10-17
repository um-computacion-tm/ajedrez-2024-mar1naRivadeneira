import unittest
from chess.board import Board
from chess.pawn import Pawn


class TestPawn(unittest.TestCase):

    def setUp(self):
        """Inicializa el tablero y peones para las pruebas."""
        self.board = Board(for_test=True) 
        self.white_pawn = Pawn("WHITE", self.board)
        self.black_pawn = Pawn("BLACK", self.board) 
    
    def test_possible_moves_white_pawn_initial(self):
        """Prueba los movimientos iniciales posibles del peón blanco.
        Verifica que el peón blanco se pueda mover una casilla hacia adelante y que no permanezca en su posición original.
        """
        self.board.set_piece(6, 4, self.white_pawn)
        moves = self.white_pawn.get_possible_pawn_moves(6, 4)
        self.assertIn((5, 4), moves)
        self.assertNotIn((6, 4), moves)
        
    def test_possible_moves_black_pawn_initial(self):
        """Prueba los movimientos iniciales posibles del peón negro.
        Verifica que el peón negro pueda moverse una o dos casillas hacia adelante desde su posición inicial.
        """
        self.board.set_piece(1, 4, self.black_pawn)
        moves = self.black_pawn.get_possible_pawn_moves(1, 4)
        expected_moves = [(2, 4), (3, 4)]
        self.assertEqual(moves, expected_moves)   
        
    def test_double_step_move_white_pawn(self):
        """Prueba el movimiento doble del peón blanco desde su posición inicial.
        Verifica que el peón blanco pueda moverse dos casillas hacia adelante desde su posición inicial.
        """
        self.board.set_piece(6, 4, self.white_pawn)
        moves= self.white_pawn.double_step_move(6, 4)
        self.assertIn((4, 4), moves)     
        
    def test_double_step_move_black_pawn(self):
        """Prueba el movimiento doble del peón negro desde su posición inicial.
        Verifica que el peón negro pueda moverse dos casillas hacia adelante desde su posición inicial.
        """
        self.board.set_piece(1, 4, self.black_pawn)
        moves= self.black_pawn.double_step_move(1, 4)
        self.assertIn((3, 4), moves)   
        
    def test_capture_move_diagonal_white(self):
        """Prueba el movimiento de captura diagonal del peón blanco.
        Verifica que el peón blanco pueda capturar una pieza negra en diagonal.
        """
        black_pawn = Pawn("BLACK", self.board)
        self.board.set_piece(5, 3, black_pawn) 
        self.board.set_piece(6, 4, self.white_pawn)    
        capture_moves =self.white_pawn.capture_move_diagonal(6, 4, [(-1, 1), (-1, -1)])
        self.assertIn((5, 3), capture_moves)
    
    def test_capture_move_diagonal_black(self):
        """Prueba el movimiento de captura diagonal del peón negro.
        Verifica que el peón negro pueda capturar una pieza blanca en diagonal.
        """
        white_pawn = Pawn("WHITE", self.board)
        self.board.set_piece(2, 3, white_pawn) 
        self.board.set_piece(1, 4, self.black_pawn)    
        capture_moves =self.black_pawn.capture_move_diagonal(1, 4, [(1, 1), (1, -1)])
        self.assertIn((2, 3), capture_moves)   
        
   
             
if __name__ == '__main__':
    unittest.main()
