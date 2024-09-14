import unittest
from chess.rook import Rook
from chess.board import Board
from chess.pawn import Pawn

class TestRook(unittest.TestCase):

    def test_str(self):
        board = Board()
        rook = Rook("WHITE", board)
        self.assertEqual(
            str(rook),
            "♖",
        )
                         
    def test_move_vertical_desc(self):
        board = Board()
        rook = Rook("WHITE", board)
        possibles = rook.possible_positions_vd(4, 1)
        self.assertEqual(
            possibles,
            [(5, 1)]
        )

    def test_move_vertical_asc(self):
        board = Board()
        rook = Rook("WHITE", board)
        possibles = rook.possible_positions_va(4, 1)
        self.assertEqual(
            possibles,
            [(3, 1), (2, 1), (1, 1)]
        )

    def test_move_vertical_desc_with_own_piece(self):
        board = Board()
        board.set_piece(6, 1, Pawn("WHITE", board))
        rook = Rook("WHITE", board)
        board.set_piece(4, 1, rook)
        possibles = rook.possible_positions_vd(4, 1)
        self.assertEqual(
            possibles,
            [(5, 1)]
        )

    def test_move_vertical_desc_with_not_own_piece(self):
        board = Board()
        board.set_piece(6, 1, Pawn("BLACK", board))
        rook = Rook("WHITE", board)
        board.set_piece(4, 1, rook)
        possibles = rook.possible_positions_vd(4, 1)
        self.assertEqual(
            possibles,
            [(5, 1), (6, 1)]
        )
        
    def test_move_horizontal_derecha(self):
        board = Board(for_test=True)
        rook = Rook("WHITE", board)  
        possibles = rook.possible_positions_hd(5, 1)
        self.assertEqual(
            possibles,
            [(5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7)]
        )
    
    def test_move_horizontal_izquierda(self):
        board = Board(for_test=True)
        rook = Rook("WHITE", board)  
        possibles = rook.possible_positions_ha(5, 7)
        self.assertEqual(
            possibles,
            [(5, 6), (5, 5), (5, 4), (5, 3), (5, 2), (5, 1), (5, 0)]
        )
    
    def test_move_horizontal_derecha_with_own_piece(self):
        board = Board(for_test=True)
        board.set_piece(5, 5, Pawn("WHITE", board))
        rook = Rook("WHITE", board)
        board.set_piece(5, 1, rook)
        possibles = rook.possible_positions_hd(5, 1)
        self.assertEqual(
            possibles,
            [(5, 2), (5, 3), (5, 4)]
        )
        
    def test_move_horizontal_derecha_with_not_own_piece(self):
        board = Board(for_test=True)
        board.set_piece(5, 5, Pawn("BLACK", board))
        rook = Rook("WHITE", board)
        board.set_piece(5, 1, rook)
        possibles = rook.possible_positions_hd(5, 1)
        self.assertEqual(
            possibles,
            [(5, 2), (5, 3), (5, 4), (5, 5)]
        )
        
    def test_move_horizontal_izquierda_with_own_piece(self):
        board = Board(for_test=True)
        board.set_piece(5, 3, Pawn("WHITE", board))
        rook = Rook("WHITE", board)
        board.set_piece(5, 7, rook)  
        possibles = rook.possible_positions_ha(5, 7)
        self.assertEqual(
            possibles,
            [(5, 6), (5, 5), (5, 4)]
        )

    def test_move_horizontal_izquierda_with_not_own_piece(self):
        board = Board(for_test=True)
        board.set_piece(5, 3, Pawn("BLACK", board))
        rook = Rook("WHITE", board)
        board.set_piece(5, 7, rook)     
        possibles = rook.possible_positions_ha(5, 7)
        self.assertEqual(
            possibles,
            [(5, 6), (5, 5), (5, 4), (5, 3)]
        )
        
    def test_move_diagonal_desc(self):
        board = Board()
        rook = board.get_piece(col=0, row=0)
        is_possible = rook.valid_positions(
            from_row=0,
            from_col=0,
            to_row=1,
            to_col=1,
        )

        self.assertFalse(is_possible)    
        
if __name__ == '__main__':
    unittest.main()       