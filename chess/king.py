#Similar a la reina, pero limitado a moverse una sola casilla en cualquier dirección. 
from chess.piece import Piece

class King(Piece):
   white_str = "♔" 
   black_str = "♚"
   
   def get_valid_moves(self, from_row, from_col, to_row, to_col):
     # Movimientos ortogonales para la torre
     possible_move= self.calculate_moves(from_row, from_col, self.__all_directions__, single_step=True)
     return (to_row, to_col)in possible_move
   