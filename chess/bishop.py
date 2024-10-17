
from chess.piece import Piece

class Bishop(Piece):
   white_str = "♗"  
   black_str = "♝"
   
   def get_valid_moves(self, from_row, from_col, to_row, to_col):
     """Verifica si un movimiento es válido para el alfil.
        Args:
            from_row (int): Fila de origen.
            from_col (int): Columna de origen.
            to_row (int): Fila de destino.
            to_col (int): Columna de destino.
        
        Returns:
            bool: True si el movimiento es válido, False de lo contrario."""
     possible_move= self.general_moves(from_row, from_col, self.get_directions(), single_step=False)
     return (to_row, to_col)in possible_move
  
   def get_directions(self):
      """Devuelve las direcciones de movimiento válidas para el alfil (diagonales).
        Returns:
            list of tuple: Lista de direcciones válidas."""
      return self.__bishop_directions__
   
   