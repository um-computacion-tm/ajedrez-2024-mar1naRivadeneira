#puede moverse en vertical o horizontal en cualquier casilla pero de la misma columna o fila
from chess.piece import Piece   

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
            #movimientos horizontales y verticales
            self.possible_positions_vd(from_row, from_col) +
            self.possible_positions_va(from_row, from_col) +
            self.possible_positions_hd(from_row, from_col) +
            self.possible_positions_ha(from_row, from_col)
         )
         return (to_row, to_col) in possible_positions
     
   def possible_positions_vd(self, row, col):
       #vertical descendente(moverse  hacia abajo en la misma columna)
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
       #vertical ascendente(se mueve hacia arriba en la misma columna)
        possibles = []
        for next_row in range(row - 1, -1, -1):
            other_piece = self.__board__.get_piece(next_row, col)
            if other_piece is not None:
                if other_piece.__color__ != self.__color__:
                    possibles.append((next_row, col))
                break  
            possibles.append((next_row, col))
        return possibles
    
   def possible_positions_hd(self, row, col):
       #horizontal hacia la derecha (moverse hacia la derecha en la misma fila)
        possibles = []
        for next_col in range(col +1, 8):
            other_piece = self.__board__.get_piece(row, next_col)
            if other_piece is not None:
                if other_piece.__color__ != self.__color__:
                    possibles.append((row, next_col))
                break
            possibles.append((row, next_col))
        return possibles    
            
   def possible_positions_ha(self, row, col):
       #horizontal izquierda (moverse hacia la izquierda en la misma fila) 
        possibles = []
        for next_col in range(col - 1, -1, -1):
            other_piece = self.__board__.get_piece(row, next_col)
            if other_piece is not None:
                if other_piece.__color__ != self.__color__:
                    possibles.append((row, next_col))
                break  
            possibles.append((row, next_col))
        return possibles
    