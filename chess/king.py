 
from chess.piece import Piece

class King(Piece):
   white_str = "♔" 
   black_str = "♚"
   
   def get_valid_moves(self, from_row, from_col, to_row, to_col):
      """Verifica si un movimiento es válido para el rey.
         Args:
               from_row (int): Fila de origen.
               from_col (int): Columna de origen.
               to_row (int): Fila de destino.
               to_col (int): Columna de destino.
         Returns:
               bool: True si el movimiento es válido, False de lo contrario."""
      return (to_row, to_col) in self.calculate_king_moves(from_row, from_col)
   
   def calculate_king_moves(self, from_row, from_col):
      """Calcula los movimientos válidos para el rey, limitados a un paso en cualquier dirección.
            Args:
               from_row (int): Fila de origen.
               from_col (int): Columna de origen.
            
            Returns:
               list of tuple: Lista de movimientos válidos."""
      return self.calculate_moves(from_row, from_col, self.__all_directions__, single_step=True)