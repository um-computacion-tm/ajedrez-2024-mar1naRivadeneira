
from chess.piece import Piece

class Pawn(Piece):
     white_str = "♙" 
     black_str = "♟"
   
     def get_valid_moves(self, from_row, from_col, to_row, to_col):
        """Verifica si un movimiento es válido para el peón.
        Args:
            from_row (int): Fila de origen.
            from_col (int): Columna de origen.
            to_row (int): Fila de destino.
            to_col (int): Columna de destino.
        
        Returns:
            bool: True si el movimiento es válido, False de lo contrario."""
        return (to_row, to_col) in self.get_possible_pawn_moves(from_row, from_col)
     
     def get_possible_pawn_moves(self, from_row, from_col):
          """Calcula todos los movimientos posibles para el peón.
               Args:
                    from_row (int): Fila de origen.
                    from_col (int): Columna de origen.
               Returns:
                    list of tuple: Lista de movimientos válidos."""
          moves=[] 

          directions, capture_directions = self.get_directions()
         
          #movimientos generales hacia adelante sin captura
          moves.extend(self.general_moves(from_row, from_col, directions, single_step=True))   
          
          #capturas diagonales
          moves.extend(self.capture_move_diagonal(from_row, from_col, capture_directions))
          
           #movimiento doble desde la fila inicial
          if not self.has_moved:
            moves.extend(self.double_step_move(from_row, from_col))
          
          return moves
     
     def get_directions(self):
          """Define las direcciones de movimiento para el peón dependiendo de su color.
        
          Returns:
               tuple: Direcciones de movimiento y de captura."""
          if self.__color__== "WHITE":
               return[(-1, 0)], [(-1, 1), (-1, -1)] #peon blanco
          else:
               return[(1, 0)], [(1, 1), (1, -1)]#peon negro
        
     def capture_move_diagonal(self, row, col, capture_directions):  
          """Calcula los movimientos de captura en diagonal para el peón.
        
          Args:
               row (int): Fila actual.
               col (int): Columna actual.
               capture_directions (list of tuple): Direcciones de captura.
          
          Returns:
               list of tuple: Lista de movimientos de captura válidos."""  
          capture_moves = []     
          for dir_row, dir_col in capture_directions:
               next_row, next_col = row + dir_row, col + dir_col
               if self.is_in_bounds(next_row, next_col) and self.can_eat(next_row, next_col):
                    capture_moves.append((next_row, next_col))
          return capture_moves
         
     def double_step_move(self, from_row, from_col):
         """Calcula el movimiento doble para el peón si está en su posición inicial.
        
          Args:
               from_row (int): Fila de origen.
               from_col (int): Columna de origen.
          
          Returns:
               list of tuple: Movimiento doble si es posible."""
         moves = []
         if self.__color__ == "BLACK" and from_row ==1:
              if self.is_in_bounds(from_row + 2, from_col) and not self.__board__.get_piece(from_row + 2, from_col):
                   moves.append((from_row +2, from_col))
         elif self.__color__== "WHITE" and from_row == 6:
              if self.is_in_bounds(from_row -2, from_col) and not self.__board__.get_piece(from_row -2, from_col):
                   moves.append((from_row -2, from_col))
                   
         return moves               

     
