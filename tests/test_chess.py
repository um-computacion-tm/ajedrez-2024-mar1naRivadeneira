import unittest
from chess import Chess



class TestChess(unittest.TestCase):
    def test_change_turn(self):
        chess=Chess()
        self.assertEqual(chess._Chess__turn__, "WHITE")
        chess.change_turn()
        self.assertEqual(chess._Chess__turn__, "BLACK")
        chess.change_turn()
        self.assertEqual(chess._Chess__turn__, "WHITE")
        
if __name__ == '__main__':
    unittest.main()                