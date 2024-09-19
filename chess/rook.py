#puede moverse en vertical o horizontal en cualquier casilla pero de la misma columna o fila
from chess.piece import Piece   

class Rook(Piece):
   white_str = "♖"  
   black_str = "♜"    
   
   
   '''def valid_positions_rook(self, from_row, from_col, to_row, to_col):
      return self.possible_orthogonal_positions( from_col, from_row)'''
      
   def possible_orthogonal_positions(self, from_row, from_col, to_row, to_col,):
        
        possible_positions = (
            #movimientos horizontales y verticales
            self.possible_positions_vd(from_row, from_col) +
            self.possible_positions_va(from_row, from_col) +
            self.possible_positions_hd(from_row, from_col) +
            self.possible_positions_ha(from_row, from_col)
         )
        return (to_row, to_col) in possible_positions   