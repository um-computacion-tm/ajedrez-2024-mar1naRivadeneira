#puede moverse en vertical o horizontal en cualquier casilla pero de la misma columna o fila
from chess.piece import Piece   

class Rook(Piece):
   white_str = "♖"  
   black_str = "♜"    
   
      
   def possible_moves_orthogonal(self, from_row, from_col, to_row, to_col):
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Vertical y horizontal
        possible_positions = self.general_moves(from_row, from_col, directions, single_step=False)
        return(to_row, to_col) in possible_positions
   
   '''def possible_orthogonal_positions(self, from_row, from_col, to_row, to_col,):
        #lista de metodos para los movimientos ortogonales = verticales y horizontales
        orthogonal_methods = (
            #movimientos horizontales y verticales
            self.possible_positions_vd, #movimiento vertical descendent
            self.possible_positions_va, #moimiento vertical ascendente
            self.possible_positions_hd, #movimiento horizontal derecha
            self.possible_positions_ha, #movimiento horizontal izquierda
         )
        
        possible_positions = self.combine_possible_positions(orthogonal_methods, from_row, from_col)
        return (to_row, to_col) in possible_positions  ''' 