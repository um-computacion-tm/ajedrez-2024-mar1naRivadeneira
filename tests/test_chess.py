import unittest
from chess.ajedrez import Chess
from chess.rook import Rook
from chess.excepciones import InvalidMove, InvalidTurn, EmptyPosition,  SamePosition
from chess.board import Board
from chess.pawn import Pawn

class TestChess(unittest.TestCase):
    """Tests para la clase Chess, que cubren el comportamiento de los movimientos y cambios de turno."""
    
    def setUp(self):
        """Configuración inicial para los tests, crea una instancia de Chess con el tablero de prueba."""
        self.chess = Chess(for_test=True)
        
    def test_show_board(self):
        """Verifica que el método show_board devuelva la representación correcta del tablero."""
        chess = Chess()
               
        tablero_esperado = (
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
        
        tablero_actual = chess.show_board() 
        self.assertEqual(tablero_actual, tablero_esperado) 
        
    def test_change_turn(self):
        """Verifica que el turno cambie correctamente entre jugadores."""
        if self.chess.turn != "WHITE":
            self.fail(f"El turno inicial debería ser 'WHITE', pero fue {self.chess.turn}")
        
        self.chess.change_turn()
        if self.chess.turn != "BLACK":
            self.fail(f"El turno debería haber cambiado a 'BLACK', pero fue {self.chess.turn}")
        
        self.chess.change_turn()
        if self.chess.turn != "WHITE":
            self.fail(f"El turno debería haber cambiado a 'WHITE', pero fue {self.chess.turn}")

    def test_raise_empty_position(self):
        """Verifica que se lance la excepción EmptyPosition al mover desde una posición vacía."""
        try:
            self.chess.move(3, 3, 4, 4)
        except EmptyPosition:
            pass
        else:
            self.fail("Se esperaba la excepción EmptyPosition, pero no se lanzó.")

    def test_raise_invalid_turn(self):
        """Verifica que se lance la excepción InvalidTurn cuando no es el turno correcto."""
        try:
            self.chess.move(0, 0, 1, 0)
        except InvalidTurn:
            pass
        else:
            self.fail("Se esperaba la excepción InvalidTurn, pero no se lanzó.")

    def test_raise_invalid_move(self):
        """Verifica que se lance la excepción InvalidMove al intentar un movimiento inválido."""
        self.chess.__board__.set_piece(0, 0, Rook("WHITE", self.chess.__board__))

        try:
            self.chess.move(0, 0, 2, 2)  
        except InvalidMove:
            pass
        else:
            self.fail("Se esperaba la excepción InvalidMove, pero no se lanzó.")

    def test_valid_move_and_turn_change(self):
        """
        Verifica que un movimiento válido se ejecute correctamente y cambie de turno.

        Coloca una torre blanca en (0, 0) y la mueve a (0, 1).
        """
        self.chess.__board__.set_piece(0, 0, Rook("WHITE", self.chess.__board__))
        
        self.chess.__turn__ = "WHITE"
        
        self.chess.move(0, 0, 0, 1)
        
        piece_in_new_position = self.chess.__board__.get_piece(0, 1)
        piece_in_old_position = self.chess.__board__.get_piece(0, 0)
        
        if piece_in_new_position is None or piece_in_old_position is not None:
            self.fail("El movimiento válido no se ejecutó correctamente.")
        
        if self.chess.turn != "BLACK":
            self.fail("El turno no cambió correctamente después de un movimiento válido.")

    def test_move_raises_game_ended_exception(self):
        """Verifica que se lance una excepción cuando el juego ha terminado."""
        self.chess.__playing__ = False
        
        try:
            self.chess.move(0, 0, 1, 0)  
        except Exception as e:
            self.assertEqual(str(e), "el juego ha terminado.")
        else:
            self.fail("Se esperaba la excepción 'el juego ha terminado', pero no se lanzó.")

    def test_end_by_agreement_ends_game(self):
        """Verifica que el juego termine correctamente por acuerdo."""
        self.assertTrue(self.chess.is_playing())
        
        self.chess.end_by_agreement()
        
        self.assertFalse(self.chess.is_playing())
        
    def test_check_end_game_white_no_pieces(self):
        """
            Verifica que el juego termine y las negras ganen cuando las blancas no tienen piezas.

            Simula un escenario en el que todas las piezas blancas han sido eliminadas del tablero.
            El resultado esperado es que las negras ganen y el juego termine.
            """
        # Simular que las blancas no tienen piezas
        for col in range(8):
            self.chess.__board__.set_piece(6, col, None)  # Eliminar los peones blancos
        self.chess.__board__.set_piece(7, 0, None)  # Eliminar torre blanca
        self.chess.__board__.set_piece(7, 1, None)  # Eliminar caballo blanco
        self.chess.__board__.set_piece(7, 2, None)  # Eliminar alfil blanco
        self.chess.__board__.set_piece(7, 3, None)  # Eliminar reina blanca
        self.chess.__board__.set_piece(7, 4, None)  # Eliminar rey blanco
        self.chess.__board__.set_piece(7, 5, None)  # Eliminar alfil blanco
        self.chess.__board__.set_piece(7, 6, None)  # Eliminar caballo blanco
        self.chess.__board__.set_piece(7, 7, None)  # Eliminar torre blanca

        result = self.chess.check_end_game()
        
        self.assertEqual(result, "BLACK")
        self.assertFalse(self.chess.is_playing())

    def test_check_end_game_black_no_pieces(self):
        """Verifica que el juego termine y las blancas ganen cuando las negras no tienen piezas.
            Simula un escenario en el que todas las piezas negras han sido eliminadas del tablero.
            El resultado esperado es que las blancas ganen y el juego termine.
            """
        # Simular que las negras no tienen piezas
        for col in range(8):
            self.chess.__board__.set_piece(1, col, None)  # Eliminar los peones negros
        self.chess.__board__.set_piece(0, 0, None)  # Eliminar torre negra
        self.chess.__board__.set_piece(0, 1, None)  # Eliminar caballo negro
        self.chess.__board__.set_piece(0, 2, None)  # Eliminar alfil negro
        self.chess.__board__.set_piece(0, 3, None)  # Eliminar reina negra
        self.chess.__board__.set_piece(0, 4, None)  # Eliminar rey negro
        self.chess.__board__.set_piece(0, 5, None)  # Eliminar alfil negro
        self.chess.__board__.set_piece(0, 6, None)  # Eliminar caballo negro
        self.chess.__board__.set_piece(0, 7, None)  # Eliminar torre negra

        result = self.chess.check_end_game()
        
        self.assertEqual(result, "WHITE")
        self.assertFalse(self.chess.is_playing())    
        
if __name__ == '__main__':
    unittest.main()                