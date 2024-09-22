#movimiento inicial de dos casillas, captura en diagonal
from chess.piece import Piece

class Pawn(Piece):
     white_str = "♙" 
     black_str = "♟"
   
#PROMOTE: cuando el peon llega al final del tablero se convierte en una reina/rey y se valida en el peon, no en el board o chess

#movimiento del peon
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
          return []