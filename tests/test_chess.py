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
            "♜♞♝♛♚♝♞♜\n"    
            "♟♟♟♟♟♟♟♟\n"  
            "        \n"
            "        \n"
            "        \n"
            "        \n"
            "♙♙♙♙♙♙♙♙\n" 
            "♖♘♗♕♔♗♘♖\n"          
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

        
    '''def test_change_turn(self): #comprueba el cambio de turno entre jugadores 
        #test para verificar que el turno cambia de  blanco a negro
        self.assertEqual(self.chess.turn, "WHITE")
        self.chess.change_turn()
        self.assertEqual(self.chess.turn, "BLACK")
        
        #test pars verificar que el turno cambia de negro a blanco
        self.chess.change_turn()
        self.assertEqual(self.chess.turn, "WHITE")
        
    def test_change_turn(self):
        """Prueba si el turno cambia correctamente después de un movimiento válido."""
        self.chess.__board__.set_piece(6, 0, Pawn("WHITE", self.chess.__board__))  # Peón blanco
        self.chess.move(6, 0, 5, 0)  # Movimiento válido de peón blanco
        self.assertEqual(self.chess.turn, "BLACK")  # El turno debería haber cambiado a "BLACK"
        
    def test_raise_empty_position(self):
        try:
            self.chess.move(3, 3, 4, 4)
        except EmptyPosition:
            pass                 #si se captura la excepcion, la prueba pasa
        else:
            self.fail("se esperaba excepcion Empty position pero no se lanzo")
            
    def test_raise_invalid_turn(self):
        try:
            self.chess.move(0, 0, 1, 0)
        except InvalidTurn:
            pass
        else:
            self.fail("se esperaba la excepcion InvalidTurn pero no se lanzo")    
            
    def test_raise_invalid_move(self):
       self.chess.__board__.set_piece(0, 0, Rook("WHITE", self.chess.__board__))
       with self.assertRaises(InvalidMove):
           self.chess.move(0, 0, 2, 2)'''


if __name__ == '__main__':
    unittest.main()                