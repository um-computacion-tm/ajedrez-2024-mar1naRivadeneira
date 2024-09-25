#Movimientos diagonales en línea recta, similares a la torre pero en las diagonales.
from chess.piece import Piece

class Bishop(Piece):
   white_str = "♗"  
   black_str = "♝"
   
   def possible_moves_diagonales(self, from_row, from_col, to_row, to_col):
      directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]  # Diagonal
      possible_positions = self.general_moves(from_row, from_col, directions, single_step=False)
      return(to_row, to_col) in possible_positions
   
   '''def possible_diagonal_positions(self, from_row, from_col, to_col, to_row):
      
      diagonal_methods = (
         self.possible_positions_dai, #Diagonal ascendente izquierda
         self.possible_positions_dad, #Diagonal ascendente derecha
         self.possible_positions_ddi,#Diagonal descendente izquierda
         self.possible_positions_ddd,  #Diagonal desscendente derecha
      )
      
      possible_positions = self.combine_possible_positions(diagonal_methods, from_row, from_col)
      return (to_row, to_col) in possible_positions'''