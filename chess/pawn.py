#movimiento inicial de dos casillas, captura en diagonal, al llegar a la ultima fila se vuelve una reina "promote"
from chess.piece import Piece
from chess.queen import Queen

class Pawn(Piece):
     white_str = "♙" 
     black_str = "♟"
   
     def get_valid_moves(self, from_row, from_col, to_row, to_col):
          # Obtener posibles movimientos y capturas
        possible_positions = self.get_possible_pawn_moves(from_row, from_col)
        return (to_row, to_col) in possible_positions
     
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
        
          #aca se verifica si el peón llega a la última fila para promoverse a reina
          for move in moves:
               to_row, to_col =move
               self.verify_promote(from_row, from_col, to_row, to_col)
          
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

          
          #aca se verifica si el peón llega a la última fila para promoverse a reina
     def verify_promote(self, from_row, from_col, to_row, to_col):
           if (self.__color__ == "WHITE" and to_row == 0) or (self.__color__ == "BLACK" and to_row == 7):
                 self.promote(to_row, to_col)
     
     def promote(self, row, col): #coloca una reina en la posicion de la promocion
        self.__board__.set_piece(row, col, Queen(self.__color__, self.__board__))
        return True #ocurrio el promote de un peon
     
'''#movimiento del peon
     def get_possible_positions(self, from_row, from_col):
        possibles = self.get_possible_positions_move(
            from_row,
            from_col,
        )
        possibles.extend(
            self.get_possible_positions_eat(from_row, from_col)
        )
        return possibles
     
     #capturas del peon
     
     def get_possible_positions_eat(self, from_row, from_col):
          #captura diagonal derecha
          possibles = []
          if self.__color__ == "BLACK":
               other_piece = self.__board__.get_piece(from_row + 1, from_col + 1)
               if other_piece and other_piece.__color__ == "WHITE":
                         possibles.append((from_row + 1, from_col + 1))    
          # Captura diagonal izquierda
               if self.__board__.in_bounds(from_row + 1, from_col - 1):
                    other_piece = self.__board__.get_piece(from_row + 1, from_col - 1)
                    if other_piece and other_piece.__color__ == "WHITE":
                         possibles.append((from_row + 1, from_col - 1))
          else:  # Para el peón blanco
               # Captura diagonal derecha
               if self.__board__.in_bounds(from_row - 1, from_col + 1):
                    other_piece = self.__board__.get_piece(from_row - 1, from_col + 1)
                    if other_piece and other_piece.__color__ == "BLACK":
                         possibles.append((from_row - 1, from_col + 1))
               # Captura diagonal izquierda
               if self.__board__.in_bounds(from_row - 1, from_col - 1):
                    other_piece = self.__board__.get_piece(from_row - 1, from_col - 1)
                    if other_piece and other_piece.__color__ == "BLACK":
                         possibles.append((from_row - 1, from_col - 1))
          return possibles
     
     def get_possible_positions_move(self, from_row, from_col):
          if self.__color__ == "BLACK":
               if self.__board__.get_piece(from_row + 1, from_col) is None:
                    if (
                         from_row == 1 and
                         self.__board__.get_piece(from_row + 2, from_col) is None
                    ):
                         return [
                         (from_row + 1, from_col),
                         (from_row + 2, from_col)
                         ]
                    else:
                         return [
                         (from_row + 1, from_col),
                         ]
          else:
               if from_row == 6:
                    return [
                         (from_row - 1, from_col),
                         (from_row - 2, from_col)
                    ]
               else:
                    if self.__board__.get_piece(from_row - 1, from_col) is None:
                         return [
                         (from_row - 1, from_col),
                         ]
                    else:
                         return []
          return []'''