import unittest
from chess.king import King
from chess.board import Board
from chess.pawn import Pawn

class TestKing(unittest.TestCase):
    """Pruebas para el comportamiento de la pieza Rey en el juego de ajedrez."""

    def setUp(self):
        """Configuración del tablero para las pruebas.
            Crea un tablero de ajedrez en modo de prueba.
            """
        self.board = Board(for_test=True)

    def test_str(self):
        """Prueba la representación en cadena del Rey.
        Verifica que el Rey se represente correctamente con el símbolo de ajedrez.
        """
        king = King("WHITE", self.board)
        self.assertEqual(
            str(king),
            "♔",
        )

    def test_king_one_step_vertical_asc(self):
        """Prueba un movimiento válido del Rey un paso hacia arriba.
        Verifica que el Rey pueda moverse un paso verticalmente hacia arriba.
        """
        king = King("WHITE", self.board)
        possibles = king.get_valid_moves(4, 4, 3, 4)
        self.assertTrue(possibles)

    def test_king_one_step_vertical_desc(self):
        """Prueba un movimiento válido del Rey un paso hacia abajo."""
        king = King("WHITE", self.board)
        possibles = king.get_valid_moves(4, 4, 5, 4)
        self.assertTrue(possibles)

    def test_king_one_step_horizontal_derecha(self):
        """Prueba un movimiento válido del Rey un paso hacia la derecha."""
        king = King("WHITE", self.board)
        possibles = king.get_valid_moves(4, 4, 4, 5)
        self.assertTrue(possibles)

    def test_king_one_step_horizontal_izquierda(self):
        """Prueba un movimiento válido del Rey un paso hacia la izquierda."""
        king = King("WHITE", self.board)
        possibles = king.get_valid_moves(4, 4, 4, 3)
        self.assertTrue(possibles)

    def test_king_one_step_diagonal_asc_derecha(self):
        """Prueba un movimiento válido del Rey en diagonal ascendente hacia la derecha."""
        king = King("WHITE", self.board)
        possibles = king.get_valid_moves(4, 4, 3, 5)
        self.assertTrue(possibles)

    def test_king_one_step_diagonal_asc_izquierda(self):
        """Prueba un movimiento válido del Rey en diagonal ascendente hacia la izquierda."""
        king = King("WHITE", self.board)
        possibles = king.get_valid_moves(4, 4, 3, 3)
        self.assertTrue(possibles)

    def test_king_one_step_diagonal_desc_derecha(self):
        """Prueba un movimiento válido del Rey en diagonal descendente hacia la derecha."""
        king = King("WHITE", self.board)
        possibles = king.get_valid_moves(4, 4, 5, 5)
        self.assertTrue(possibles)

    def test_king_one_step_diagonal_desc_izquierda(self):
        """Prueba un movimiento válido del Rey en diagonal descendente hacia la izquierda."""
        king = King("WHITE", self.board)
        possibles = king.get_valid_moves(4, 4, 5, 3)
        self.assertTrue(possibles)

    def test_king_invalid_move_two_steps_vertical(self):
        """Prueba un movimiento no válido del Rey de dos pasos verticales."""
        king = King("WHITE", self.board)
        possibles = king.get_valid_moves(4, 4, 2, 4)
        self.assertFalse(possibles)

    def test_king_invalid_move_two_steps_horizontal(self):
        """Prueba un movimiento no válido del Rey de dos pasos horizontales."""
        king = King("WHITE", self.board)
        possibles = king.get_valid_moves(4, 4, 4, 6)
        self.assertFalse(possibles)

    def test_king_move_with_blocking_own_piece(self):
        """Prueba un movimiento no válido del Rey bloqueado por una pieza propia."""
        self.board.set_piece(3, 3, Pawn("WHITE", self.board))
        king = King("WHITE", self.board)
        self.board.set_piece(4, 4, king)
        possibles = king.get_valid_moves(4, 4, 3, 3)
        self.assertFalse(possibles)

    def test_king_move_with_blocking_opponent_piece(self):
        """Prueba un movimiento válido del Rey capturando una pieza oponente."""
        self.board.set_piece(3, 3, Pawn("BLACK", self.board))
        king = King("WHITE", self.board)
        self.board.set_piece(4, 4, king)
        possibles = king.get_valid_moves(4, 4, 3, 3)
        self.assertTrue(possibles)

if __name__ == '__main__':
    unittest.main()
