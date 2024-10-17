import unittest
from chess.knight import Knight
from chess.board import Board
from  chess.pawn import Pawn

class TestKnight(unittest.TestCase):

    def setUp(self):
        """Inicializa el tablero para las pruebas."""
        self.board = Board(for_test=True)

    def test_str(self):
        """Prueba la representación en cadena del Caballo.
        Verifica que la representación en string del Caballo sea el símbolo correcto.
        """
        knight = Knight("WHITE", self.board)
        self.assertEqual(
            str(knight),
            "♘",
        )

    def test_valid_move_L_shape_up_right(self):
        """Prueba un movimiento válido en forma de L (arriba-derecha).
        Verifica que el Caballo pueda moverse dos casillas arriba y una a la derecha.
        """
        knight = Knight("WHITE", self.board)
        possibles = knight.get_valid_moves(4, 4, 2, 5)
        self.assertTrue(possibles)

    def test_valid_move_L_shape_up_left(self):
        """Prueba un movimiento válido en forma de L (arriba-izquierda).
        Verifica que el Caballo pueda moverse dos casillas arriba y una a la izquierda.
        """
        knight = Knight("WHITE", self.board)
        possibles = knight.get_valid_moves(4, 4, 2, 3)
        self.assertTrue(possibles)

    def test_valid_move_L_shape_down_right(self):
        """Prueba un movimiento válido en forma de L (abajo-derecha).
        Verifica que el Caballo pueda moverse dos casillas abajo y una a la derecha.
        """
        knight = Knight("WHITE", self.board)
        possibles = knight.get_valid_moves(4, 4, 6, 5)
        self.assertTrue(possibles)

    def test_valid_move_L_shape_down_left(self):
        """Prueba un movimiento válido en forma de L (abajo-izquierda).
        Verifica que el Caballo pueda moverse dos casillas abajo y una a la izquierda.
        """
        knight = Knight("WHITE", self.board)
        possibles = knight.get_valid_moves(4, 4, 6, 3)
        self.assertTrue(possibles)

    def test_valid_move_L_shape_right_up(self):
        """Prueba un movimiento válido en forma de L (derecha-arriba).
        Verifica que el Caballo pueda moverse dos casillas a la derecha y una hacia arriba.
        """
        knight = Knight("WHITE", self.board)
        possibles = knight.get_valid_moves(4, 4, 3, 6)
        self.assertTrue(possibles)

    def test_valid_move_L_shape_right_down(self):
        """Prueba un movimiento válido en forma de L (derecha-abajo).
        Verifica que el Caballo pueda moverse dos casillas a la derecha y una hacia abajo.
        """
        knight = Knight("WHITE", self.board)
        possibles = knight.get_valid_moves(4, 4, 5, 6)
        self.assertTrue(possibles)

    def test_valid_move_L_shape_left_up(self):
        """Prueba un movimiento válido en forma de L (izquierda-arriba).
        Verifica que el Caballo pueda moverse dos casillas a la izquierda y una hacia arriba.
        """
        knight = Knight("WHITE", self.board)
        possibles = knight.get_valid_moves(4, 4, 3, 2)
        self.assertTrue(possibles)

    def test_valid_move_L_shape_left_down(self):
        """Prueba un movimiento válido en forma de L (izquierda-abajo).
        Verifica que el Caballo pueda moverse dos casillas a la izquierda y una hacia abajo.
        """
        knight = Knight("WHITE", self.board)
        possibles = knight.get_valid_moves(4, 4, 5, 2)
        self.assertTrue(possibles)

    def test_invalid_move_straight(self):
        """Prueba un movimiento no válido en línea recta.
        Verifica que el Caballo no pueda moverse en línea recta.
        """
        knight = Knight("WHITE", self.board)
        possibles = knight.get_valid_moves(4, 4, 4, 6)
        self.assertFalse(possibles)

    def test_invalid_move_diagonal(self):
        """Prueba un movimiento no válido en diagonal.
        Verifica que el Caballo no pueda moverse en diagonal.
        """
        knight = Knight("WHITE", self.board)
        possibles = knight.get_valid_moves(4, 4, 6, 6)
        self.assertFalse(possibles)

    def test_move_with_blocking_own_piece(self):
        """Prueba un movimiento bloqueado por una pieza propia.
        Verifica que el Caballo no pueda saltar a una casilla ocupada por una pieza propia.
        """
        self.board.set_piece(2, 5, Pawn("WHITE", self.board))
        knight = Knight("WHITE", self.board)
        possibles = knight.get_valid_moves(4, 4, 2, 5)
        self.assertFalse(possibles)

    def test_move_with_blocking_opponent_piece(self):
        """Prueba un movimiento con captura de una pieza oponente.
        Verifica que el Caballo pueda moverse a una casilla ocupada por una pieza oponente.
        """
        self.board.set_piece(2, 5, Pawn("BLACK", self.board))
        knight = Knight("WHITE", self.board)
        possibles = knight.get_valid_moves(4, 4, 2, 5)
        self.assertTrue(possibles)

if __name__ == '__main__':
    unittest.main()
