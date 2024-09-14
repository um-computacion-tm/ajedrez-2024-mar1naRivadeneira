import unittest
from chess.piece import Piece

class TestPiece(unittest.TestCase):
    def setUp(self):
        self.piece = Piece('WHITE', None)
       
if __name__ == '__main__':
    unittest.main()       