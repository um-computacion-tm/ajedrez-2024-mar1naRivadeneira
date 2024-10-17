import unittest
from chess.rook import Rook
from chess.board import Board
from chess.pawn import Pawn

class TestRook(unittest.TestCase):
    """Pruebas para el comportamiento de la pieza Torre en el juego de ajedrez."""

    def test_str(self):
        """Prueba la representación en cadena de la Torre.
        Verifica que la Torre se represente correctamente con el símbolo de ajedrez.
        """
        board = Board()
        rook = Rook("WHITE", board)
        self.assertEqual(
            str(rook),
            "♖",
        )
                         
    def test_move_vertical_desc(self):
        """Prueba un movimiento válido de la Torre hacia abajo.
        Verifica que la Torre puede moverse hacia abajo en la columna sin restricciones.
        """
        board = Board()
        rook = Rook("WHITE", board)
        possibles = rook.get_valid_moves(4, 1, 5, 1)
        self.assertTrue(possibles)
           
    def test_move_vertical_asc(self):
        """Prueba un movimiento válido de la Torre hacia arriba.
        Verifica que la Torre puede moverse hacia arriba en la columna sin restricciones.
        """
        board = Board()
        rook = Rook("WHITE", board)
        possibles = rook.get_valid_moves(4, 1, 3, 1)
        self.assertTrue(possibles)

    def test_move_vertical_desc_with_own_piece(self):
        """Prueba un movimiento válido de la Torre hacia abajo bloqueada por una pieza propia.
        Verifica que la Torre no puede capturar o moverse a una posición ocupada por una pieza del mismo color.
        """
        board = Board()
        board.set_piece(6, 1, Pawn("WHITE", board))
        rook = Rook("WHITE", board)
        board.set_piece(4, 1, rook)
        possibles = rook.get_valid_moves(4, 1, 5, 1)
        self.assertTrue(possibles)

    def test_move_vertical_desc_with_not_own_piece(self):
        """Prueba un movimiento válido de la Torre capturando una pieza oponente al moverse hacia abajo."""
        board = Board()
        board.set_piece(6, 1, Pawn("BLACK", board))
        rook = Rook("WHITE", board)
        board.set_piece(4, 1, rook)
        possibles = rook.get_valid_moves(4, 1, 6, 1)
        self.assertTrue(possibles)
        
    def test_move_horizontal_derecha(self):
        """Prueba un movimiento válido de la Torre hacia la derecha.
        Verifica que la Torre puede moverse horizontalmente hacia la derecha sin restricciones.
        """
        board = Board(for_test=True)
        rook = Rook("WHITE", board)  
        possibles = rook.get_valid_moves(5, 1, 5, 3)
        self.assertTrue(possibles)
           
    def test_move_horizontal_izquierda(self):
        """Prueba un movimiento válido de la Torre hacia la izquierda.
        Verifica que la Torre puede moverse horizontalmente hacia la izquierda sin restricciones.
        """
        board = Board(for_test=True)
        rook = Rook("WHITE", board)  
        possibles = rook.get_valid_moves(5, 7, 5, 5)
        self.assertTrue(possibles)
           
    def test_move_horizontal_derecha_with_own_piece(self):
        """Prueba un movimiento no válido de la Torre bloqueada por una pieza propia a la derecha.
        Verifica que la Torre no puede capturar o moverse a una posición ocupada por una pieza del mismo color.
        """
        board = Board(for_test=True)
        board.set_piece(5, 5, Pawn("WHITE", board))
        rook = Rook("WHITE", board)
        board.set_piece(5, 1, rook)
        possibles = rook.get_valid_moves(5, 1, 5, 3)
        self.assertTrue(possibles)
        
    def test_move_horizontal_derecha_with_not_own_piece(self):
        """Prueba un movimiento válido de la Torre capturando una pieza oponente hacia la derecha.
        Verifica que la Torre puede moverse hacia la derecha y capturar una pieza oponente.
        """
        board = Board(for_test=True)
        board.set_piece(5, 5, Pawn("BLACK", board))
        rook = Rook("WHITE", board)
        board.set_piece(5, 1, rook)
        possibles = rook.get_valid_moves(5, 1, 5, 5)
        self.assertTrue(possibles)
        
    def test_move_horizontal_izquierda_with_own_piece(self):
        """Prueba un movimiento no válido de la Torre bloqueada por una pieza propia hacia la izquierda.
        Verifica que la Torre no puede moverse hacia la izquierda si una pieza del mismo color bloquea el camino.
        """
        board = Board(for_test=True)
        board.set_piece(5, 3, Pawn("WHITE", board))
        rook = Rook("WHITE", board)
        board.set_piece(5, 7, rook)  
        possibles = rook.get_valid_moves(5, 7, 5, 4)
        self.assertTrue(possibles)
        
    def test_move_horizontal_izquierda_with_not_own_piece(self):
        """Prueba un movimiento válido de la Torre capturando una pieza oponente hacia la izquierda.
        Verifica que la Torre puede moverse hacia la izquierda y capturar una pieza oponente.
        """
        board = Board(for_test=True)
        board.set_piece(5, 3, Pawn("BLACK", board))
        rook = Rook("WHITE", board)
        board.set_piece(5, 7, rook)     
        possibles = rook.get_valid_moves(5, 7, 5, 3)
        self.assertTrue(possibles)
        
    def test_move_diagonal_desc(self):
        """Prueba un movimiento no válido de la Torre en diagonal.
        Verifica que la Torre no puede moverse en diagonal, ya que su movimiento solo es permitido en líneas rectas.
        """
        board = Board()
        rook = board.get_piece(col=0, row=0)
        is_possible = rook.get_valid_moves(
            from_row=0,
            from_col=0,
            to_row=1,
            to_col=1,
        )

        self.assertFalse(is_possible)
        
if __name__ == '__main__':
    unittest.main()    