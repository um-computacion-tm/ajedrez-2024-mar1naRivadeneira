import unittest
from chess.chess import Chess



class TestChess(unittest.TestCase):
    
    def setUp(self):
        self.chess = Chess()
        
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
        self.chess.move(0, 0, 1, 0)
        
        #comprueba que el turno cambio
        new_turn = self.chess.turn
        self.assertNotEqual(new_turn, turno_inicial)    
        self.assertEqual(new_turn, "BLACK")
        
if __name__ == '__main__':
    unittest.main()                