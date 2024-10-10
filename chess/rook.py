#puede moverse en vertical o horizontal en cualquier casilla pero de la misma columna o fila
from chess.piece import Piece   

class Rook(Piece):
  white_str = "♖"  
  black_str = "♜"    
   
  def get_valid_moves(self, from_row, from_col, to_row, to_col):
      directions = self.is_valid_rook_move()
      possible_moves = self.general_moves(from_row, from_col, directions, single_step=False )
      return (to_row, to_col) in possible_moves

    
  def is_valid_rook_move(self): 
     # Movimientos ortogonales para la torre
     return [(-1, 0), (1, 0), (0, -1), (0, 1)]