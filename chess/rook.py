#puede moverse en vertical o horizontal en cualquier casilla pero de la misma columna o fila
from chess.piece import Piece   

class Rook(Piece):
   white_str = "♖"  
   black_str = "♜"    
   
   
   def possible_orthogonal_positions(self, from_row, from_col):
       return(
           #movimientos horizontales y verticales
            self.possible_positions_vd(from_row, from_col) +  #Vertical descendente
            self.possible_positions_va(from_row, from_col) +  #Vertical ascendente
            self.possible_positions_hd(from_row, from_col) +  #Horizontal derecha
            self.possible_positions_ha(from_row, from_col)    #Horizontal izquierda
       )
       