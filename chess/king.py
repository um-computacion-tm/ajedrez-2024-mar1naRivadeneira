 
from chess.piece import Piece

class King(Piece):
   white_str = "♔" 
   black_str = "♚"
   
   def get_valid_moves(self, from_row, from_col, to_row, to_col):
      """Calcula si una posición de destino es válida para el Rey.

        El Rey se puede mover en cualquier dirección (horizontal, vertical o diagonal),
        pero solo una casilla a la vez. Este método utiliza todas las direcciones posibles
        y limita los movimientos a un solo paso.

        Parámetros:
        - from_row (int): La fila de origen de la pieza.
        - from_col (int): La columna de origen de la pieza.
        - to_row (int): La fila de destino donde se desea mover la pieza.
        - to_col (int): La columna de destino donde se desea mover la pieza.

        Retorna:
        - bool: `True` si la posición de destino es válida para el movimiento del Rey,
                `False` en caso contrario.
               """
      positions = self.__all_directions__         
      possible_king_positions = self.calculate_moves(from_row, from_col, positions, single_step = True)
      return (to_row, to_col) in possible_king_positions
   
   