import unittest
from chess import Chess



class TestChess(unittest.TestCase):
    
    def setUp(self):
        self.__game__ = Chess()
        
    def test_initial_turn(self):
        self.assertEqual(self.__game__.turn, "WHITE" , "El turno debe ser de las blancas")

        
if __name__ == '__main__':
    unittest.main()                