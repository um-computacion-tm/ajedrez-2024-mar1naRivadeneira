#Similar a la reina, pero limitado a moverse una sola casilla en cualquier dirección. 
from chess.piece import Piece

class King(Piece):
   white_str = "♔" 
   black_str = "♚"
   
   def possible_moves_king(self, from_row, from_col, to_row, to_col):
      directions = [
            (1, 0), (-1, 0), (0, 1), (0, -1),
            (1, 1), (1, -1), (-1, 1), (-1, -1)
      ]
      possible_positions = self.general_moves(from_row, from_col, directions, single_step=True)
      return(to_row, to_col) in possible_positions
   