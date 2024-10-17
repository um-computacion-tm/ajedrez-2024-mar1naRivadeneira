 
from chess.piece import Piece

class King(Piece):
   white_str = "♔" 
   black_str = "♚"
   
   def get_valid_moves(self, from_row, from_col, to_row, to_col):
      """Verifica si el movimiento solicitado es válido para el Rey.
        Parámetros:
         from_row : int
               Fila de la posición inicial del Rey.
         from_col : int
               Columna de la posición inicial del Rey.
         to_row : int
               Fila de la posición destino.
         to_col : int
               Columna de la posición destino.

         Retorna:
         --------
         bool:
               True si el movimiento es válido, False en caso contrario.
               """
      return (to_row, to_col) in self.calculate_king_moves(from_row, from_col)
   
   def calculate_king_moves(self, from_row, from_col):
      """Calcula los movimientos válidos para el rey, limitados a un paso en cualquier dirección.
            Args:
               from_row (int): Fila de origen.
               from_col (int): Columna de origen.
            
            Returns:
               list of tuple: Lista de movimientos válidos."""
      return self.calculate_moves(from_row, from_col, self.__all_directions__, single_step=True)