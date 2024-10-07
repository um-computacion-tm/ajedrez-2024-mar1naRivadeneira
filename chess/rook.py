#puede moverse en vertical o horizontal en cualquier casilla pero de la misma columna o fila
from chess.piece import Piece   

class Rook(Piece):
  white_str = "♖"  
  black_str = "♜"    
   
  def get_valid_moves(self, from_row, from_col, to_row, to_col):
      return self.is_valid_rook_move(from_row, from_col, to_row, to_col)
    
  def is_valid_rook_move(self, from_row, from_col, to_row, to_col): 
     # Movimientos ortogonales para la torre
     possible_move= self.general_moves(from_row, from_col, self.__rook_directions__, single_step=False)
     return (to_row, to_col)in possible_move