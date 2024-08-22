import unittest
from chess.chess import Chess



class TestChess(unittest.TestCase):
    
    def setUp(self):
        self.__game__ = Chess()
        
    def test_initial_turn(self):
        self.assertEqual(self.__game__.__turn__, "WHITE" , "El turno debe ser de las blancas")

        
if __name__ == '__main__':
    unittest.main()                