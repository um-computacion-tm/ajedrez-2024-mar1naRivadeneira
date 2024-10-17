import unittest
from chess.bishop import Bishop
from chess.board import Board

class TestBishop(unittest.TestCase):
    """Pruebas unitarias para la pieza Bishop(Alfil)."""
    
    def setUp(self):
        """Configura un tablero para pruebas."""
        self.board = Board(for_test = True)
    
    def test_str(self):
        """Prueba que la representación en string del Alfil sea correcta."""
        board = Board()
        bishop = Bishop("WHITE", board)
        self.assertEqual(
            str(bishop),
            "♗",
        )
    
    def test_move_diagonal_asc_izquierda(self):
        """Verifica movimientos válidos en diagonal ascendente hacia la izquierda."""
        bishop = Bishop("WHITE", self.board)
        possibles = bishop.get_valid_moves(3, 3, 0, 0)
        self.assertTrue(possibles)
     
    def test_move_diagonal_asc_derecha(self):
        """Verifica movimientos válidos en diagonal ascendente hacia la derecha."""
        bishop = Bishop("WHITE", self.board)
        possibles = bishop.get_valid_moves(4, 4, 2, 6)
        self.assertTrue(possibles)
        
    def test_move_diagonal_desc_izquierda(self):
        """Verifica movimientos válidos en diagonal descendente hacia la izquierda."""
        bishop = Bishop("WHITE", self.board)
        possibles = bishop.get_valid_moves(4, 4, 7, 1)
        self.assertTrue(possibles)
        
    def test_move_diagonal_desc_derecha(self):
        """Verifica movimientos válidos en diagonal descendente hacia la derecha"""
        bishop = Bishop("WHITE", self.board)
        possibles = bishop.get_valid_moves(4, 4, 6, 6)
        self.assertTrue( possibles,)
        
    def test_move_diagonal_asc_izquierda_with_own_piece(self):
        """Prueba si un movimiento está bloqueado por una pieza propia en diagonal ascendente hacia la izquierda."""
        self.board.set_piece(2, 2, Bishop("WHITE", self.board))
        bishop = Bishop("WHITE", self.board)
        self.board.set_piece(5, 5, bishop)
        possibles = bishop.get_valid_moves(5, 5, 3, 3)
        self.assertTrue(possibles) 
        
    def test_move_diagonal_asc_izquierda_with_opponent_piece(self):
        """Prueba si un movimiento incluye captura de pieza contraria en diagonal ascendente hacia la izquierda."""
        self.board.set_piece(3, 3, Bishop("BLACK", self.board))
        bishop = Bishop("WHITE", self.board)
        self.board.set_piece(4, 4, bishop)
        possibles = bishop.get_valid_moves(4, 4, 3, 3)
        self.assertTrue(possibles)               
     
    def test_move_diagonal_asc_derecha_with_own_piece(self):
        """Prueba un movimiento diagonal ascendente hacia la derecha bloqueado por una pieza propia.
        Verifica que el alfil no pueda moverse si una pieza propia está en la casilla de destino."""
        self.board.set_piece(3, 5, Bishop("WHITE", self.board))
        bishop = Bishop("WHITE", self.board)
        self.board.set_piece(4, 4, bishop)
        possibles = bishop.get_valid_moves(4, 4, 5, 5)                      
        self.assertTrue(possibles)
        
    def test_move_diagonal_asc_derecha_with_opponent_piece(self):
        """Prueba un movimiento diagonal ascendente hacia la derecha con captura de una pieza oponente.
        Verifica que el alfil pueda moverse y capturar una pieza oponente en la casilla de destino."""
        self.board.set_piece(3, 5, Bishop("BLACK", self.board))
        bishop = Bishop("WHITE", self.board)
        self.board.set_piece(4, 4, bishop)
        possibles = bishop.get_valid_moves(4, 4, 3, 5)
        self.assertTrue(possibles)  
        
    def test_move_diagonal_desc_izquierda_with_own_piece(self):
        """Prueba un movimiento diagonal descendente hacia la izquierda bloqueado por una pieza propia.
        Verifica que el alfil no pueda moverse si una pieza propia bloquea el camino."""
        self.board.set_piece(6, 2, Bishop("WHITE", self.board))
        bishop = Bishop("WHITE", self.board)
        self.board.set_piece(4, 4, bishop)
        possibles = bishop.get_valid_moves(4, 4, 5, 3)
        self.assertTrue(possibles)
        
    def test_move_diagonal_desc_derecha_with_opponent_piece(self):
        """Prueba un movimiento diagonal descendente hacia la derecha con captura de una pieza oponente.
        Verifica que el alfil pueda capturar una pieza oponente en la casilla de destino."""
        self.board.set_piece(6, 6, Bishop("BLACK", self.board))
        bishop = Bishop("WHITE", self.board)
        self.board.set_piece(4, 4, bishop)
        possibles = bishop.get_valid_moves(4, 4, 6, 6)
        self.assertTrue(possibles)
          
if __name__ == '__main__':
    unittest.main()       