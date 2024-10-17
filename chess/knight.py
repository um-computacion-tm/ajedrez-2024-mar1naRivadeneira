
from chess.piece import Piece

class Knight(Piece): 
   white_str = "♘"  
   black_str = "♞"
  
   def get_valid_moves(self, from_row, from_col, to_row, to_col):
       """Verifica si un movimiento es válido para el caballo.
        
            Args:
                from_row (int): Fila de origen.
                from_col (int): Columna de origen.
                to_row (int): Fila de destino.
                to_col (int): Columna de destino.
            
            Returns:
                bool: True si el movimiento es válido, False de lo contrario."""
       possible_moves = self.calculate_moves(from_row, from_col)
       return (to_row, to_col) in possible_moves
   
   def calculate_moves(self, from_row, from_col):
        """Calcula los movimientos válidos del caballo en forma de "L".
            Args:
                from_row (int): Fila de origen.
                from_col (int): Columna de origen.
            
            Returns:
                list of tuple: Lista de movimientos válidos."""
        valid_moves = []
        
        for row_offset in [-2, -1, 1, 2]:
            col_offset = 3 - abs(row_offset)
            for col_delta in [-col_offset, col_offset]:
                new_row = from_row + row_offset
                new_col = from_col + col_delta
                
                if self.is_in_bounds(new_row, new_col):
                    if self.can_eat(new_row, new_col) or self.__board__.get_piece(new_row, new_col) is None:
                        valid_moves.append((new_row, new_col))
        return valid_moves                
                