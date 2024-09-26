#movimiento inicial de dos casillas, captura en diagonal, al llegar a la ultima fila se vuelve una reina "promote"
from chess.piece import Piece
from chess.queen import Queen


class Pawn(Piece):
     white_str = "♙" 
     black_str = "♟"
   
     def possible_moves(self, row, col):
          directions = [(1, 0)]  

          # direcciones según el color del peón
          if self.__color__ == "WHITE":
               directions = [(-1, 0)]  # movimiento hacia adelante blanco
               capture_directions = [(-1, 1), (-1, -1)]  #captura en diagonal
          else:
               directions = [(1, 0)]  # movimiento hacia adelante negro
               capture_directions = [(1, 1), (1, -1)] 
               
          #movimientos generales hacia adelante sin captura
          moves = self.general_moves(row, col, directions, single_step=True)
          
          #cappturas diagonales
          for dir_row, dir_col in capture_directions:
               next_row, next_col = row + dir_row, col + dir_col
               if 0 <= next_row < 8 and 0 <= next_col < 8 and self.can_eat(next_row, next_col):
                    moves.append((next_row, next_col))
          
          #movimiento doble desde la fila inicial
          if self.__color__ == "WHITE" and row == 6 and not self.is_occupied(row - 1, col):
               if not self.is_occupied(row - 2, col):
                    moves.append((row - 2, col))
          elif self.__color__ == "BLACK" and row == 1 and not self.is_occupied(row + 1, col):
               if not self.is_occupied(row + 2, col):
                    moves.append((row + 2, col))

          return moves

    

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