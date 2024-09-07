import unittest
from chess.chess import Chess
from chess.excepciones import InvalidMove, InvalidTurn, EmptyPosition


class TestChess(unittest.TestCase):
    
    def setUp(self):
        self.chess = Chess()
        
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
        
        
    def test_change_turn(self): #comprueba el cambio de turno entre jugadores 
        #test para verificar que el turno cambia de  blanco a negro
        self.assertEqual(self.chess.turn, "WHITE")
        self.chess.change_turn()
        self.assertEqual(self.chess.turn, "BLACK")
        
        #test pars verificar que el turno cambia de negro a blanco
        self.chess.change_turn()
        self.assertEqual(self.chess.turn, "WHITE")
        
    def test_move_changes_turn(self):#verifica el cambio de turno despues de un movimiento
        #comprobar el turno incial
        turno_inicial = self.chess.turn
        self.assertEqual(turno_inicial, "WHITE")
        
        #realizo un movimiento
        self.chess.move(7, 0, 5, 0)
        
        #comprueba que el turno cambio
        new_turn = self.chess.turn
        self.assertNotEqual(new_turn, turno_inicial)    
        self.assertEqual(new_turn, "BLACK")
        
    def test_raise_empty_position(self):
        try:
            self.chess.move(3, 3, 4, 4)
        except EmptyPosition:
            pass                 #si se captura la excepcion, la prueba pasa
        else:
            self.fail("se esperaba excepcion Empty position pero no se lanzo")
            
    def test_raise_invalid_move(self):
        try:
            self.chess.move(0, 0, 1, 1)
        except InvalidMove:
            pass
        else:
            self.fail("se esperaba la excepcion InvalidMove pero no se lanzo")            
            
    
if __name__ == '__main__':
    unittest.main()                