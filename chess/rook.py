#puede moverse en vertical o horizontal en cualquier casilla pero de la misma columna o fila
from chess.piece import Piece   
#from exceptions import InvalidMoveRookMove  (importar las excepciones)  aca levantamos la excepcion y en el CLI la atrapamos

class Rook(Piece):
   white_str = "♖"  
   black_str = "♜"    
   
   def valid_positions(
         self,
         from_row,
         from_col,
         to_row,
         to_col,
   ):
         possible_positions = (
            self.possible_positions_vd(from_row, from_col) +
            self.possible_positions_va(from_row, from_col)
         )
         return (to_row, to_col) in possible_positions

   def possible_positions_vd(self, row, col):
        possibles = []
        for next_row in range(row + 1, 8):
            # que la celda que sigue no este ocupada..
            other_piece = self.__board__.get_piece(next_row, col)
            if other_piece is not None:
                if other_piece.__color__ != self.__color__:
                    possibles.append((next_row, col))
                break
            possibles.append((next_row, col))
        return possibles

   def possible_positions_va(self, row, col):
        possibles = []
        for next_row in range(row - 1, -1, -1):
            possibles.append((next_row, col))
        return possibles
