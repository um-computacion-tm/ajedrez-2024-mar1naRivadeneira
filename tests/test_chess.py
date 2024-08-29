import unittest
from chess.chess import Chess



class TestChess(unittest.TestCase):
    
    def setUp(self):
        self.chess = Chess()
        
    def test_change_turn(self): 
        #test para verificar que el turno cambia de  blanco a negro
        self.assertEqual(self.chess.turn, "WHITE")
        self.chess.change_turn()
        self.assertEqual(self.chess.turn, "BLACK")
        
        #test pars verificar que el turno cambia de negro a blanco
        self.chess.change_turn()
        self.assertEqual(self.chess.turn, "WHITE")
        
if __name__ == '__main__':
    unittest.main()                