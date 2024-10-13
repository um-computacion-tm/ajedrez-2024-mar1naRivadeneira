#movimiento inicial de dos casillas, captura en diagonal, al llegar a la ultima fila se vuelve una reina "promote"
from chess.piece import Piece

class Pawn(Piece):
     white_str = "♙" 
     black_str = "♟"
   
     def get_valid_moves(self, from_row, from_col, to_row, to_col):
          # Obtener posibles movimientos y capturas
        return (to_row, to_col) in self.get_possible_pawn_moves(from_row, from_col)
     
     def get_possible_pawn_moves(self, from_row, from_col):
          moves=[] 

          # direcciones según el color del peón
          directions, capture_directions = self.get_directions()
         
          #movimientos generales hacia adelante sin captura
          moves.extend(self.general_moves(from_row, from_col, directions, single_step=True))   
          
          #cappturas diagonales
          moves.extend(self.capture_move_diagonal(from_row, from_col, capture_directions))
          
           #movimiento doble desde la fila inicial
          if not self.has_moved:
            moves.extend(self.double_step_move(from_row, from_col))
          
          return moves
     
     def get_directions(self):
          if self.__color__== "WHITE":
               return[(-1, 0)], [(-1, 1), (-1, -1)] #peon blanco
          else:
               return[(1, 0)], [(1, 1), (1, -1)]#peon negro
        
     def capture_move_diagonal(self, row, col, capture_directions):    
          #captura en diagonal
          capture_moves = []     
          for dir_row, dir_col in capture_directions:
               next_row, next_col = row + dir_row, col + dir_col
               if self.is_in_bounds(next_row, next_col) and self.can_eat(next_row, next_col):
                    capture_moves.append((next_row, next_col))
          return capture_moves
         
     def double_step_move(self, from_row, from_col):
         moves = []
         if self.__color__ == "BLACK" and from_row ==1:
              if self.is_in_bounds(from_row + 2, from_col) and not self.__board__.get_piece(from_row + 2, from_col):
                   moves.append((from_row +2, from_col))
         elif self.__color__== "WHITE" and from_row == 6:
              if self.is_in_bounds(from_row -2, from_col) and not self.__board__.get_piece(from_row -2, from_col):
                   moves.append((from_row -2, from_col))
                   
         return moves               

     
