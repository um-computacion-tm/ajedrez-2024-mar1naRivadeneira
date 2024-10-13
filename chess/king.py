#Similar a la reina, pero limitado a moverse una sola casilla en cualquier dirección. 
from chess.piece import Piece

class King(Piece):
   white_str = "♔" 
   black_str = "♚"
   
   def get_valid_moves(self, from_row, from_col, to_row, to_col):
      return (to_row, to_col) in self.calculate_king_moves(from_row, from_col)
   
   def calculate_king_moves(self, from_row, from_col):
        # Solo permite un paso en cada dirección
        return self.calculate_moves(from_row, from_col, self.__all_directions__, single_step=True)