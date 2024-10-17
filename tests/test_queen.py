import unittest
from chess.queen import Queen 
from chess.board import Board
from chess.pawn import Pawn

class TestQueen(unittest.TestCase):
    """Pruebas para el comportamiento de la pieza Reina en el juego de ajedrez."""
    
    def setUp(self):
        """Configuración del tablero para las pruebas."""
        self.board = Board(for_test=True)

    def test_str(self):
        """Prueba la representación en cadena de la Reina.
        Verifica que la Reina se represente correctamente con el símbolo de ajedrez.
        """
        queen = Queen("WHITE", self.board)
        self.assertEqual(
            str(queen),
            "♕",
        )

    def test_move_queen_vertical_asc(self):
        """Prueba un movimiento válido de la Reina en dirección vertical ascendente."""
        queen = Queen("WHITE", self.board)
        possibles = queen.get_valid_moves(4, 1, 2, 1)
        self.assertTrue(possibles)

    def test_move_queen_vertical_desc(self):
        """Prueba un movimiento válido de la Reina en dirección vertical descendente."""
        queen = Queen("WHITE", self.board)
        possibles = queen.get_valid_moves(4, 1, 6, 1)
        self.assertTrue(possibles)

    def test_move_queen_horizontal_derecha(self):
        """Prueba un movimiento válido de la Reina en dirección horizontal hacia la derecha."""
        queen = Queen("WHITE", self.board)
        possibles = queen.get_valid_moves(4, 4, 4, 7)
        self.assertTrue(possibles)

    def test_move_queen_horizontal_izquierda(self):
        """Prueba un movimiento válido de la Reina en dirección horizontal hacia la izquierda."""
        queen = Queen("WHITE", self.board)
        possibles = queen.get_valid_moves(4, 4, 4, 0)
        self.assertTrue(possibles)

    def test_move_queen_diagonal_asc_derecha(self):
        """Prueba un movimiento válido de la Reina en diagonal ascendente hacia la derecha.
        Verifica que la Reina pueda moverse en diagonal ascendente hacia la derecha.
        """
        queen = Queen("WHITE", self.board)
        possibles = queen.get_valid_moves(4, 4, 2, 6)
        self.assertTrue(possibles)

    def test_move_queen_diagonal_asc_izquierda(self):
        """Prueba un movimiento válido de la Reina en diagonal ascendente hacia la izquierda.
        Verifica que la Reina pueda moverse en diagonal ascendente hacia la izquierda.
        """
        queen = Queen("WHITE", self.board)
        possibles = queen.get_valid_moves(4, 4, 2, 2)
        self.assertTrue(possibles)

    def test_move_queen_diagonal_desc_derecha(self):
        """Prueba un movimiento válido de la Reina en diagonal descendente hacia la derecha.
        Verifica que la Reina pueda moverse en diagonal descendente hacia la derecha.
        """
        queen = Queen("WHITE", self.board)
        possibles = queen.get_valid_moves(4, 4, 6, 6)
        self.assertTrue(possibles)

    def test_move_queen_diagonal_desc_izquierda(self):
        """Prueba un movimiento válido de la Reina en diagonal descendente hacia la izquierda.
        Verifica que la Reina pueda moverse en diagonal descendente hacia la izquierda.
        """
        queen = Queen("WHITE", self.board)
        possibles = queen.get_valid_moves(4, 4, 6, 2)
        self.assertTrue(possibles)

    def test_move_queen_with_blocking_own_piece(self):
        """Prueba un movimiento no válido de la Reina bloqueada por una pieza propia.
        Verifica que la Reina no pueda moverse a una casilla ocupada por una pieza del mismo color.
        """
        self.board.set_piece(5, 5, Pawn("WHITE", self.board))
        queen = Queen("WHITE", self.board)
        self.board.set_piece(4, 4, queen)
        possibles = queen.get_valid_moves(4, 4, 6, 6)
        self.assertFalse(possibles)

    def test_move_queen_with_blocking_opponent_piece(self):
        """Prueba un movimiento válido de la Reina capturando una pieza oponente.
        Verifica que la Reina pueda moverse a una casilla ocupada por una pieza del oponente.
        """
        self.board.set_piece(6, 6, Pawn("BLACK", self.board))
        queen = Queen("WHITE", self.board)
        self.board.set_piece(4, 4, queen)
        possibles = queen.get_valid_moves(4, 4, 6, 6)
        self.assertTrue(possibles)

if __name__ == '__main__':
    unittest.main()
