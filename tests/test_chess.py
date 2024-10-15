import unittest
from chess.ajedrez import Chess
from chess.rook import Rook
from chess.excepciones import InvalidMove, InvalidTurn, EmptyPosition,  SamePosition
from chess.board import Board
from chess.pawn import Pawn

class TestChess(unittest.TestCase):
    
    def setUp(self):
        self.chess = Chess(for_test=True)
        
    def test_show_board(self):
        chess = Chess()
            
        #lo que se espera que devuelva    
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
        self.assertEqual(tablero_actual, tablero_esperado) #compara la salida esperada con la salida real
        
    def test_change_turn(self):
        if self.chess.turn != "WHITE":
            self.fail(f"El turno inicial debería ser 'WHITE', pero fue {self.chess.turn}")
        
        self.chess.change_turn()
        if self.chess.turn != "BLACK":
            self.fail(f"El turno debería haber cambiado a 'BLACK', pero fue {self.chess.turn}")
        
        self.chess.change_turn()
        if self.chess.turn != "WHITE":
            self.fail(f"El turno debería haber cambiado a 'WHITE', pero fue {self.chess.turn}")

    def test_raise_empty_position(self):
        try:
            self.chess.move(3, 3, 4, 4)
        except EmptyPosition:
            pass
        else:
            self.fail("Se esperaba la excepción EmptyPosition, pero no se lanzó.")

    def test_raise_invalid_turn(self):
        try:
            self.chess.move(0, 0, 1, 0)
        except InvalidTurn:
            pass
        else:
            self.fail("Se esperaba la excepción InvalidTurn, pero no se lanzó.")

    def test_raise_invalid_move(self):
        self.chess.__board__.set_piece(0, 0, Rook("WHITE", self.chess.__board__))

        try:
            self.chess.move(0, 0, 2, 2)  # Intentar mover la torre en diagonal
        except InvalidMove:
            pass
        else:
            self.fail("Se esperaba la excepción InvalidMove, pero no se lanzó.")

    def test_valid_move_and_turn_change(self):
        # Coloca una torre blanca en (0, 0) y mueve a (0, 1) (movimiento válido)
        self.chess.__board__.set_piece(0, 0, Rook("WHITE", self.chess.__board__))
        
        # Asegura que el turno inicial es de las blancas
        self.chess.__turn__ = "WHITE"
        
        self.chess.move(0, 0, 0, 1)
        
        # Verifica que la pieza se haya movido
        piece_in_new_position = self.chess.__board__.get_piece(0, 1)
        piece_in_old_position = self.chess.__board__.get_piece(0, 0)
        
        if piece_in_new_position is None or piece_in_old_position is not None:
            self.fail("El movimiento válido no se ejecutó correctamente.")
        
        # Verifica que el turno haya cambiado
        if self.chess.turn != "BLACK":
            self.fail("El turno no cambió correctamente después de un movimiento válido.")

    def test_move_raises_game_ended_exception(self):
        # Finalizar el juego
        self.chess.__playing__ = False
        
        try:
            self.chess.move(0, 0, 1, 0)  # Intentar mover cuando el juego ha terminado
        except Exception as e:
            self.assertEqual(str(e), "el juego ha terminado.")
        else:
            self.fail("Se esperaba la excepción 'el juego ha terminado', pero no se lanzó.")

    def test_end_by_agreement_ends_game(self):
        # Verificar que el juego esté en curso
        self.assertTrue(self.chess.is_playing())
        
        # Finalizar el juego por acuerdo
        self.chess.end_by_agreement()
        
        # Verificar que el juego ha terminado
        self.assertFalse(self.chess.is_playing())
        
    def test_check_end_game_white_no_pieces(self):
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