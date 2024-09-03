import unittest
from chess.piece import Piece

class TestPiece(unittest.TestCase):
    def setUp(self):
        self.piece = Piece('WHITE', None)
        
    def test_mover(self):
        try:
            self.piece.mover()
            print("mover fue llamado bcon exito")
        except Exception as e:
            self.fail(f"mover() raised an exception: {e}")        
        
    
    
    
    
if __name__ == '__main__':
    unittest.main()       